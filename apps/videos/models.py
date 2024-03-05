from apps.user.models import User
from django.db import models
from django.utils.timezone import now
from django.db.models.signals import pre_delete
from apps.user.models import Channel
from django.dispatch import receiver

# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='channel')
    created_date = models.DateTimeField(blank=False, default=now, editable=True)
@receiver(pre_delete, sender=Video)
def delete_post_photo(sender, instance, **kwargs):
    instance.video_file.delete()


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