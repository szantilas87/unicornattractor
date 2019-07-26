from django.urls import path
from .views import QueryListView, BugCreateView, QueryUpdateView, QueryDeleteView, UserQueryListView, FeaturesListView, BugsListView, FeatureCreateView
from . import views
from pages.query_types import query_types


urlpatterns = [
    path('', QueryListView.as_view(extra_context={'query_types': query_types}), name='home'),
    path('user/<str:username>', UserQueryListView.as_view(), name='user-queries'),
    path('query/<int:id>', views.query_detail, name='query-detail'),
    path('query/new-bug/', BugCreateView.as_view(), name='bug-create'),
    path('query/new-feature/', FeatureCreateView.as_view(), name='feature-create'),
    path('query/<int:pk>/update', QueryUpdateView.as_view(), name='query-update'),
    path('query/<int:pk>/delete', QueryDeleteView.as_view(), name='query-delete'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('like/', views.like_query, name='like_query'),
    path('paid/', views.paid, name='paid'),
    path('features/', FeaturesListView.as_view(), name='features'),
    path('bugs/', BugsListView.as_view(), name='bugs'),

]
