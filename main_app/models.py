from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse

WHALE_SPECIES = (
    ('1', 'Select Species'),
    ('2', 'Orca'),
    ('3', 'Minke'),
    ('4', 'Humpback'),
    ('5', 'Blue'),
    ('6', 'Sperm'),
    ('7', 'Beluga'),
    ('8', 'Gray'),
    ('9', 'Fin'),
    ('10', 'Dolphin'),
    ('11', 'Seal'),
    ('12', 'Sea Lion'),
    ('13', 'Sea Otter'),
    ('14', 'Other'),
    ('15', 'Unknown')
)
class Sighting(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField('sighting date')
    latitude = models.DecimalField(max_digits=12, decimal_places=9)
    longitude = models.DecimalField(max_digits=12, decimal_places=9)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    species = models.CharField(
        max_length=2,
        choices=WHALE_SPECIES,
        default=WHALE_SPECIES[0][0]
    )
    likes = models.ManyToManyField(User, related_name='sighting_likes', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

    def has_comments(self):
        return self.comment_set

    def has_likes(self):
        return self.likes.count()

    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    text = models.TextField('comment', max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    sighting = models.ForeignKey(Sighting, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)

    def __str__(self):
        return str(self.text)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

    def has_likes(self):
        return self.likes.count()

    def has_replies(self):
        return self.reply.count()

    class Meta:
        ordering = ['-created_date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    sighting = models.ForeignKey(Sighting, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for sighting_id: {self.sighting_id} @{self.url}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Profile of user {self.user.username}"

class Reply(models.Model):
    text = models.TextField('comment', max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.text)