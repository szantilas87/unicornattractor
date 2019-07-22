from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Query

#Main page view
class QueryListView(ListView):
    model = Query
    template_name = 'pages/index.html'
    context_object_name = 'queries'
    ordering = ['-date_posted']

#A view for particular query
class QueryDetailView(DetailView):
    model = Query

#Create a new query
class QueryCreateView(LoginRequiredMixin, CreateView):
    model = Query
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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