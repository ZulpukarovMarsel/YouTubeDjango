from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from apps.user.models import Channel


# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='channel')
    created_date = models.DateTimeField(blank=False, default=now, editable=True)


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_author')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f"Like from {self.author} to {self.post}"

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_author')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_date = models.DateTimeField(blank=False, default=now)

    def __str__(self):
        return f"Comment from {self.author} to {self.content}"