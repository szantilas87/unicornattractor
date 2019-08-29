from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Query, Comment
from .forms import CommentForm
from django.conf import settings
import stripe
from io import BytesIO
import base64
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import numpy as np
from django.db.models import Count
import csv
import pandas as pd
from datetime import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

class QueryListView(ListView):
    """
    Main page view
    """
    model = Query
    template_name = 'pages/index.html'
    context_object_name = 'queries' 
    ordering = ['-date_posted']
    

    def get_context_data(self, **kwargs):
        stripe.api_key = settings.STRIPE_PRIVATE_KEY
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLIC_KEY
        context['page_title']="UnicornAttractor"
        return context
       

class UserQueryListView(ListView):
    """
    List of queries for a particular user
    """
    model = Query
    template_name = 'pages/user_queries.html'
    context_object_name = 'queries'
    paginate_by = 8

    
    #Find queries for the specific user
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Query.objects.filter(author=user).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        context = super().get_context_data(**kwargs)
        context['page_title']=user.username
        return context


def query_detail(request, id):
    """
    A view for particular query
    """
    query = get_object_or_404(Query, id=id,)
    query.views += 1
    query.save()
    is_liked = False
    if query.likes.filter(id=request.user.id).exists():
        is_liked = True

    comments = Comment.objects.filter(query=query).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(query=query, user=request.user, content= content)
            
                      
            return redirect(reverse('query-detail',kwargs={"id":id}))
        
    else:
        comment_form = CommentForm()
    
    context = {
        'query': query,
        'comments': comments,
        'comment_form': comment_form,
        'is_liked': is_liked,
        'total_likes': query.total_likes(),
        'page_title': query.title
    }
    
    return render(request,'pages/query_detail.html', context)


def like_query(request):
    """
    Like query
    """
    query_id =request.POST.get('query_id')
    query = get_object_or_404(Query, id=request.POST.get('query_id'))
    is_liked = False
    if query.likes.filter(id=request.user.id).exists():
        query.likes.remove(request.user)
        is_liked = False
    else:
        query.likes.add(request.user)
        is_liked = True
    return redirect('query-detail', id=query_id)


class QueryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Update an exisiting query
    """
    model = Query
    fields = ['title', 'content']
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

   
    #Test if the logged user is the author of the query
    def test_func(self):
        query = self.get_object()
        if self.request.user == query.author:
            return True
        return False
   
    def get_success_url(self):
        query = self.get_object()
        return reverse('query-detail', kwargs={"id":query.id} )

 

class QueryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete a query
    """
    model = Query
    success_url = '/'

   
    #Test if the logged user is the author of the query
    def test_func(self):
        query = self.get_object()
        if self.request.user == query.author:
            return True
        return False

def about(request):
    """
    About page view
    """
    
    #Pie chart bugs/features ratio 
    bugs = Query.objects.filter(query_type="Bug" ).count()
    features = Query.objects.filter(query_type="Feature").count()
    slices = [bugs, features]
    labels = ['Bugs', 'Features']
    colors = ['#008fd5', '#fc4f30']
    explode = [0, 0.1]
    fig1, ax1 = plt.subplots()

    ax1.pie(slices, labels=labels, colors=colors,explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%')

    fig1.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    piechart = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    buf.close()

    
    #Bar chart for status of the queries
    to_do = Query.objects.filter(status='To do').count()
    in_progress= Query.objects.filter(status='In progess').count()
    done = Query.objects.filter(status='Done').count()    
    statuses = [ to_do, in_progress, done]
    x_axis = np.arange(3)
    labels = ['To do', 'In progress', 'Done']
    colors = ('#6d904f', '#fc4f30', '#008fd5')
    fig2, ax2 = plt.subplots()

   
    ax2.bar(x_axis, statuses, color=colors)

    ax2.set_xticks(ticks=x_axis)
    ax2.set_xticklabels(labels=labels)

    for a,b in zip(x_axis, statuses):
        ax2.text(a, b, str(b), ha='center', va='bottom')
    
    ax2.set_xlabel('Status')
    ax2.set_ylabel('Amount')

    yint = []
    locs, labels = plt.yticks()                                       
    for each in locs:
        yint.append(int(each))
    plt.yticks(yint)

    

    
    fig2.tight_layout()
    
    buf = BytesIO()
    plt.savefig(buf, format='png')
    statuschart = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    buf.close()

    
    #Amount of queries in time
    queries = Query.objects.all()
    fieldnames = ['date']

    with open('media/charts/raw_data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        
        for each in queries:
            date = {"date":each.date_posted.strftime("%d-%m-%Y")}
            csv_writer.writerow(date)

    fig3, ax3 = plt.subplots()

    ax2.set_ylabel('Amount')
    
    raw_data = pd.read_csv('media/charts/raw_data.csv')
    aggregate_dates = raw_data.groupby(['date']).size().to_frame('amount')
    aggregate_dates.to_csv('media/charts/data_calculated.csv')

    data = pd.read_csv('media/charts/data_calculated.csv')

    data['date'] = pd.to_datetime(data['date'],format= '%d-%m-%Y')
    data.sort_values('date', inplace=True)

    date = data['date']
    amount = data['amount']

    ax3.plot_date(date, amount, linestyle='solid')
    ax3.set_ylabel('Amount')
    plt.gcf().autofmt_xdate()
 
    yint = []
    locs, labels = plt.yticks()                                       
    for each in locs:
        yint.append(int(each))
    plt.yticks(yint)

  

    fig3.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    datechart = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
    buf.close()



    context = {
        'page_title':'About',
        'piechart': piechart,
        'statuschart':statuschart,
        'datechart':datechart
    }
    
    
    return render(request, 'pages/about.html', context)



def search(request):
    """
    Search view
    """
    queries = Query.objects.order_by('-date_posted')
    paginator = Paginator(queries, 8)
    page = request.GET.get('page')
    paged_queries = paginator.get_page(page)

    
    #Search for keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queries = queries.filter(content__icontains=keywords) or queries.filter(title__icontains=keywords)
    
    context = {
        'queries': queries,
        'page_title':'Search results' 
    }
    return render(request, 'pages/search.html', context)


def paid(request):
    """
    Access to adding a feature after payment
    """
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=5000,
            currency='usd',
            description='Features access',
            source=request.POST['stripeToken']
        )
        return render(request, 'pages/paid.html',  {'page_title':'Thank you'})