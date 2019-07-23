from django.urls import path
from .views import QueryListView, QueryCreateView, QueryUpdateView, QueryDeleteView, UserQueryListView
from . import views
from pages.query_types import query_types

urlpatterns = [
    path('', QueryListView.as_view(extra_context={'query_types': query_types}), name='home'),
    path('user/<str:username>', UserQueryListView.as_view(), name='user-queries'),
    path('query/<int:id>', views.query_detail, name='query-detail'),
    path('query/new/', QueryCreateView.as_view(), name='query-create'),
    path('query/<int:pk>/update', QueryUpdateView.as_view(), name='query-update'),
    path('query/<int:pk>/delete', QueryDeleteView.as_view(), name='query-delete'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
        
]
