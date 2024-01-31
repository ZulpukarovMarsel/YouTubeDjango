from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Channel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='channel')
    subscribers = models.ManyToManyField(User, related_name='subscribed_channels', blank=True)

    def __str__(self):
        return self.name