from django.urls import path
from .views import QueryListView, QueryUpdateView, QueryDeleteView, UserQueryListView 
from . import views

urlpatterns = [
    path('', QueryListView.as_view(), name='home'),
    path('user/<str:username>', UserQueryListView.as_view(), name='user-queries'),
    path('query/<int:id>', views.query_detail, name='query-detail'),
    path('query/<int:pk>/update', QueryUpdateView.as_view(extra_context={'page_title': 'Update'}), name='query-update'),
    path('query/<int:pk>/delete', QueryDeleteView.as_view(extra_context={'page_title': 'Delete'}), name='query-delete'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('like/', views.like_query, name='like_query'),
    path('paid/', views.paid, name='paid'),
]

