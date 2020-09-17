from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sighting, Comment, Photo
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import uuid
import boto3

# constants for AWS S3 photos
S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'whalescope'


# Create views below:
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def add_photo(request, sighting_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, sighting_id=sighting_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', pk=sighting.pk)

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
    fields = ['title', 'date', 'location', 'description', 'species']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SightingUpdate(UpdateView):
    model = Sighting
    fields = ['date', 'location', 'description', 'species']

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
    if request.method == 'POST':
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


def comments_update(request, pk, comment_id):
    sighting = get_object_or_404(Sighting, pk=pk)
    if request.method == 'POST':
        if comment_id:
            form = CommentForm(instance=Comment.objects.get(id=comment_id), data=request.POST)
            form.save()
            return redirect('detail', pk=sighting.pk)
        else:
            form = CommentForm(data=request.POST)
        return redirect('detail', pk=sighting.pk)


def comments_delete(request, sighting_id, comment_id):
    context={}
    obj = get_object_or_404(Comment, id=comment_id)

    if request.method == 'GET':
        obj.delete()
        return redirect('detail', sighting_id)
