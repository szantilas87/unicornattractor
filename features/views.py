from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from pages.models import Query



#List of features
class FeaturesListView(ListView):
    model = Query
    template_name = 'pages/features_queries.html'
    context_object_name = 'queries'
    paginate_by = 8

    #Find queries with type = feature
    def get_queryset(self):
        return Query.objects.filter(query_type="Feature" ).order_by('-date_posted')



#Mixin to check whether the user has paid donation, and give access to crearte a new feature
class PaidUserOnlyMixin(object):
    def has_permissions(self):
        return self.request.user.profile.premium
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            return redirect('home')
        return super(PaidUserOnlyMixin, self).dispatch(
            request, *args, **kwargs)


#Create a new feature
class FeatureCreateView(LoginRequiredMixin, PaidUserOnlyMixin , CreateView):
    model = Query
    template_name = 'pages/new_feature.html'
    fields = ['title', 'content',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.query_type = 'Feature'
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('query-detail', kwargs={'id': self.object.pk})