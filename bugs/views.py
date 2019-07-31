from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from pages.models import Query




#List of bugs
class BugsListView(ListView):
    model = Query
    template_name = 'pages/bug_queries.html'
    context_object_name = 'queries'
    paginate_by = 8

    #Find queries with type = bug
    def get_queryset(self):
        return Query.objects.filter(query_type="Bug" ).order_by('-date_posted')

#Create a new bug
class BugCreateView(LoginRequiredMixin, CreateView):
    
    model = Query
    fields = ['title', 'content',]
    template_name = 'pages/new_bug.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.query_type = 'Bug'
        return super().form_valid(form)
    
    
    def get_success_url(self):
        return reverse('query-detail', kwargs={'id': self.object.pk})