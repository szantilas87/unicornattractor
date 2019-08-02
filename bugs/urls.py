from django.urls import path
from .views import BugCreateView
from . import views


urlpatterns = [
    path('query/new-bug', BugCreateView.as_view(), name='bug-create'),
    path('bugs', views.bugs, name='bugs')
]
