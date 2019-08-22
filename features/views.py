from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from pages.models import Query
from unicorn.sort_choices import sort_choices
from django.conf import settings
import stripe
from pages.views import paid

"""
List of features
"""
def features(request):
    queries = Query.objects.filter(query_type="Feature").order_by('-date_posted')
    sort = '-date_posted'
    paginator = Paginator(queries, 8)
    page = request.GET.get('page')
    paged_queries = paginator.get_page(page)
    key = settings.STRIPE_PUBLIC_KEY
    stripe.api_key = settings.STRIPE_PRIVATE_KEY

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
        'sort': sort,
        'key': key,
        'stripe.api_key': stripe.api_key,
        'page_title':"Features"
    }
    return render(request, 'features/features_queries.html', context)

"""
Mixin to check whether the user has paid donation, and give access to crearte a new feature
"""
class PaidUserOnlyMixin(object):
    def has_permissions(self):
        return self.request.user.profile.premium
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            return redirect('home')
        return super(PaidUserOnlyMixin, self).dispatch(
            request, *args, **kwargs)

"""
Create a new feature
"""
class FeatureCreateView(LoginRequiredMixin, PaidUserOnlyMixin , CreateView):
    model = Query
    template_name = 'features/new_feature.html'
    fields = ['title', 'content',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.query_type = 'Feature'
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('query-detail', kwargs={'id': self.object.pk})