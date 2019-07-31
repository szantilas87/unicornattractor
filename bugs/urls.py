from django.urls import path
from .views import BugCreateView, BugsListView
from . import views


urlpatterns = [
    path('query/new-bug', BugCreateView.as_view(), name='bug-create'),
    path('bugs', BugsListView.as_view(), name='bugs')
]
