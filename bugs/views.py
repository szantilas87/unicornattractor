from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from pages.models import Query
from unicorn.sort_choices import sort_choices




#List of bugs
def bugs(request):
    queries = Query.objects.filter(query_type="Bug" ).order_by('-date_posted')
    sort = '-date_posted'
    paginator = Paginator(queries, 8)
    page = request.GET.get('page')
    paged_queries = paginator.get_page(page)

    if 'sort' in request.GET:
        sort = request.GET['sort']
        if sort:
            queries = queries.order_by(sort)
            paginator = Paginator(queries, 8)
            page = request.GET.get('page')
            paged_queries = paginator.get_page(page)
        
    
    context = {
        'queries': paged_queries,
        'sort_choices' : sort_choices,
        'values': request.GET,
        'sort': sort
    }
    return render(request, 'bugs/bug_queries.html', context)

class BugCreateView(LoginRequiredMixin, CreateView):
    
    model = Query
    fields = ['title', 'content',]
    template_name = 'bugs/new_bug.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.query_type = 'Bug'
        return super().form_valid(form)
    
    
    def get_success_url(self):
        return reverse('query-detail', kwargs={'id': self.object.pk})