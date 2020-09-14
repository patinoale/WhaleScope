from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Sighting(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField('sighting date')
    location = models.CharField(max_length=100) # Need to determine how to handle this long-term
    description = models.TextField(max_length=500)
    # Need to add a species field with choices

