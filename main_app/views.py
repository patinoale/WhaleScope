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

# class CommentDelete(DeleteView):
#     model = Comment
#     success_url = '/sightings/'



def comments_delete(request, pk, comment_id):
# def comments_delete(request):
    id = request.POST.get(['comment_id'])
    pk = request.POST.get(['sighting_id'])
    # sighting = get_object_or_404(Sighting, pk=pk)
    if request.method == 'POST':
        # if comment_id:
            comment = get_object_or_404(Comment, id=id, pk=pk)
            try:
                context = {}
                comment.delete()
                return redirect('detail', context, pk=sighting.pk)
            except:
                return redirect('detail', context, pk=sighting.pk)
                    
    #         form = CommentForm(instance=Comment.objects.get(id=comment_id), data=request.POST)
    #         form.remove()
    # return redirect('detail', pk=sighting.pk)

