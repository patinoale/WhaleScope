from django.forms import ModelForm
from django.db import models
from .models import Comment, Reply

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['text']