from django.shortcuts import render
from .models import Query

def home(request):
    context = {
        'queries': Query.objects.all()
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')