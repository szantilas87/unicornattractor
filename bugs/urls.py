from django.urls import path
from .views import BugCreateView
from . import views

urlpatterns = [
    path('query/new-bug', BugCreateView.as_view(extra_context={'page_title':"Add bug"
}), name='bug-create'),
    path('bugs', views.bugs, name='bugs')
]
