from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse


# Create your models here.
class Sighting(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField('sighting date')
    location = models.CharField(max_length=100) # Need to determine how to handle this long-term
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Need to add a species field with choices

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

    def has_comments(self):
        return self.comment_set

class Comment(models.Model):
    text = models.TextField('comment', max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    sighting = models.ForeignKey(Sighting, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="reply")

    def __str__(self):
        return str(self.text)

    class Meta:
        ordering = ['-created_date']