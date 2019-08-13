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
from matplotlib import pyplot as plt
import numpy as np
from django.db.models import Count
import csv
from datetime import datetime
import pandas as pd




"""
Main page view
"""
class QueryListView(ListView):
    model = Query
    template_name = 'pages/index.html'
    context_object_name = 'queries' 
    ordering = ['-date_posted']
    

    def get_context_data(self, **kwargs):
        stripe.api_key = settings.STRIPE_PRIVATE_KEY
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLIC_KEY
        return context

   
       
"""
List of queries for a particular user
"""
class UserQueryListView(ListView):
    model = Query
    template_name = 'pages/user_queries.html'
    context_object_name = 'queries'
    paginate_by = 8

    """
    Find queries for the specific user
    """
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Query.objects.filter(author=user).order_by('-date_posted')


"""
A view for particular query
"""
def query_detail(request, id):
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
            comment_form.save()
                      
            return redirect(reverse('query-detail',kwargs={"id":id}))
        
    else:
        comment_form = CommentForm()
    
    context = {
        'query': query,
        'comments': comments,
        'comment_form': comment_form,
        'is_liked': is_liked,
        'total_likes': query.total_likes(),
    }
    
    return render(request,'pages/query_detail.html', context, )

"""
Like query
"""
def like_query(request):
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

"""
Update an exisiting query
"""
class QueryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Query
    fields = ['title', 'content']



    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    """
    Test if the logged user is the author of the query
    """
    def test_func(self):
        query = self.get_object()
        if self.request.user == query.author:
            return True
        return False

   
    def get_success_url(self):
        query = self.get_object()
        return reverse('query-detail', kwargs={"id":query.id} )


"""
Delete a query
"""
class QueryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Query
    success_url = '/'

    """
    Test if the logged user is the author of the query
    """
    def test_func(self):
        query = self.get_object()
        if self.request.user == query.author:
            return True
        return False

"""
About page view
"""
def about(request):
    """ 
    Pie chart bugs/features ratio 
    """
    bugs = Query.objects.filter(query_type="Bug" ).count()
    features = Query.objects.filter(query_type="Feature").count()

    slices = [bugs, features]
    labels = ['Bugs', 'Features']
    colors = ['#008fd5', '#fc4f30']
    explode = [0, 0.1]
    fig1, ax1 = plt.subplots()

    ax1.pie(slices, labels=labels, colors=colors,explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'}, autopct='%1.1f%%')

    fig1.tight_layout()

    fig1.savefig('media/charts/pie.png')

    """
    Bar chart for status of the queries
    """
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
    
    fig2.tight_layout()

    fig2.savefig('media/charts/status.png')

    """
    Amount of queries in time
    """
    queries = Query.objects.all()

    fieldnames = ['date']

    with open('media/charts/raw_data.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        
        for each in queries:
            date = {"date":each.date_posted.strftime("%d-%m-%Y")}
            csv_writer.writerow(date)

    fig3, ax3 = plt.subplots()
    
    raw_data = pd.read_csv('media/charts/raw_data.csv')
    aggregate_dates = raw_data.groupby(['date']).size().to_frame('amount')
    aggregate_dates.to_csv('media/charts/data_calculated.csv')

    data = pd.read_csv('media/charts/data_calculated.csv')
    date = data['date']
    amount = data['amount']

    ax3.plot_date(date, amount, linestyle='solid')
    plt.gcf().autofmt_xdate()
    fig3.tight_layout()
    fig3.savefig('media/charts/dates.png')
    
    return render(request, 'pages/about.html')


"""
Search view
"""
def search(request):
    queries = Query.objects.order_by('-date_posted')

    paginator = Paginator(queries, 8)
    page = request.GET.get('page')
    paged_queries = paginator.get_page(page)

    """
    Search for keywords
    """
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queries = queries.filter(content__icontains=keywords) or queries.filter(title__icontains=keywords)
    
    context = {
        'queries': queries,
    }
    return render(request, 'pages/search.html', context)

"""
Access to adding a feature after payment
"""
def paid(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=5000,
            currency='usd',
            description='Features access',
            source=request.POST['stripeToken']
        )
        return render(request, 'pages/paid.html')