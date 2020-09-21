from django.forms import ModelForm
from django.db import models
from .models import Comment

class CommentForm(ModelForm):
    # content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols':'50'}))
    class Meta:
        model = Comment
        fields = ['text']