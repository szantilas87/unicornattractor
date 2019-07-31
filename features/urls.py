from django.urls import path
from .views import  FeaturesListView, FeatureCreateView
from . import views



urlpatterns = [
    path('query/new-feature/', FeatureCreateView.as_view(), name='feature-create'),
    path('features/', FeaturesListView.as_view(), name='features')
]