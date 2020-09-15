from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse


# Create your models here.
class Sighting(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField('sighting date')
    location = models.CharField(max_length=100) # Need to determine how to handle this long-term
    description = models.TextField(max_length=500)
    # Need to add a species field with choices

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

class Comment(models.Model):
    text = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    sighting = models.ForeignKey(Sighting, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic
