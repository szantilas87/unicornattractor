from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Query, Comment
from .forms import CommentForm
from pages.query_types import query_types
from django.conf import settings
import stripe



#Main page view
class QueryListView(ListView):
    model = Query
    template_name = 'pages/index.html'
    context_object_name = 'queries' 
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        stripe.api_key = settings.STRIPE_PRIVATE_KEY
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLIC_KEY
        return context

   
       
#List of queries for a particular user
class UserQueryListView(ListView):
    model = Query
    template_name = 'pages/user_queries.html'
    context_object_name = 'queries'
    paginate_by = 5

    #Find queries for the specific user
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Query.objects.filter(author=user).order_by('-date_posted')

#List of features
class FeaturesListView(ListView):
    model = Query
    template_name = 'pages/features_queries.html'
    context_object_name = 'queries'
    paginate_by = 5

    #Find queries with type = feature
    def get_queryset(self):
        return Query.objects.filter(query_type="Feature" ).order_by('-date_posted')


#List of bubs
class BugsListView(ListView):
    model = Query
    template_name = 'pages/bug_queries.html'
    context_object_name = 'queries'
    paginate_by = 5

    #Find queries with type = bug
    def get_queryset(self):
        return Query.objects.filter(query_type="Bug" ).order_by('-date_posted')




#A view for particular query
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

# Like query
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


#Create a new query
class QueryCreateView(LoginRequiredMixin, CreateView):
    
    model = Query
    fields = ['title', 'content', 'query_type']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('home')


#Update an exisiting query
class QueryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
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


#Delete a query
class QueryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Query
    success_url = '/'

    #Test if the logged user is the author of the query
    def test_func(self):
        query = self.get_object()
        if self.request.user == query.author:
            return True
        return False

#About page view
def about(request):
    return render(request, 'pages/about.html')

#Search view
def search(request):
    queryset_list = Query.objects.order_by('-date_posted')

    #Search for keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(content__icontains=keywords) or queryset_list.filter(title__icontains=keywords)
    
    #Filter by type of the query
    if 'query_type' in request.GET:
        query_type = request.GET['query_type']
        if query_type:
            queryset_list = queryset_list.filter(query_type__iexact=query_type) 

    context = {
        'queries': queryset_list,
        'query_types': query_types,
        'values': request.GET,
    }
    return render(request, 'pages/search.html', context)

# Access to adding feature after payment
def paid(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=5000,
            currency='usd',
            description='Features access',
            source=request.POST['stripeToken']
        )
        return render(request, 'pages/paid.html')