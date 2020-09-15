from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse

WHALE_SPECIES = (
    ('1', 'Orca'),
    ('2', 'Minke'),
    ('3', 'Humpback'),
    ('4', 'Dolphin'),
    ('5', 'Seal'),
    ('6', 'Sea Lion'),
    ('7', 'Sea Otter'),
    ('8', 'Other'),
    ('9', 'Unknown')
)

class Sighting(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField('sighting date')
    location = models.CharField(max_length=100) # Need to determine how to handle this long-term
    description = models.TextField(max_length=500)
    # Need to add a species field with choices
    species = models.CharField(
        max_length=1,
        choices=WHALE_SPECIES,
        default=WHALE_SPECIES[0][0]
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-date']

