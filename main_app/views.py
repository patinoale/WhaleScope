from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sighting, Comment
from .forms import *
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

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


def add_comment(request, pk):
    sighting = get_object_or_404(Sighting, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.sighting = sighting
            form.save()
            return redirect('detail', pk=sighting.pk)
    else:
        form = CommentForm()
    return render(request, 'detail', {'form': form})

# class CommentCreate(CreateView):
#     model = Comment
#     form = CommentForm
#     fields = '__all__'
    
    
#     def form_valid(self, form, pk):
#         form.instance.created_by = self.request.user
#         new_comment = form.save(commit=False)
#         new_comment.sighting_id = sighting_id
#         
#         return super(CommentCreate, self, pk=sighting.pk).form_valid(form)
