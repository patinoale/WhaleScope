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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Need to add a species field with choices
    species = models.CharField(
        max_length=1,
        choices=WHALE_SPECIES,
        default=WHALE_SPECIES[0][0]
    )

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

    def __str__(self):
        return str(self.text)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-created_date']

