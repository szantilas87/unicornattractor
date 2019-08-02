from django.urls import path
from .views import FeatureCreateView
from . import views



urlpatterns = [
    path('query/new-feature/', FeatureCreateView.as_view(), name='feature-create'),
    path('features/', views.features, name='features')
]