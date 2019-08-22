from django.urls import path
from .views import FeatureCreateView
from . import views

urlpatterns = [
    path('query/new-feature/', FeatureCreateView.as_view(extra_context={'page_title':"Add feature"
}), name='feature-create'),
    path('features/', views.features, name='features')
]