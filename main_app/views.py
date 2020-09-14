from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sighting
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create views below:
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class SightingList(ListView):
    model = Sighting

class SightingDetail(DetailView):
    model = Sighting

class SightingCreate(CreateView):
    model = Sighting
    fields = '__all__'

class SightingUpdate(UpdateView):
    model = Sighting
    fields = ['date', 'location', 'description']
class SightingDelete(DeleteView):
    model = Sighting
    success_url = '/sightings/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('index')
    else:
        error_message = 'Invalid sign up - try again'
        
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)