from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sighting

# Create views below:
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class SightingList(ListView):
    model = Sighting

class SightingDetail(DetailView):
    model = Sighting