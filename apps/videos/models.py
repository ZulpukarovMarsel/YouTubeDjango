from apps.user.models import User
from django.db import models
from django.utils.timezone import now
from django.db.models.signals import pre_delete
from apps.user.models import Channel
from django.dispatch import receiver

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='channel')
    created_date = models.DateTimeField(blank=False, default=now, editable=True)

    class Meta:
        verbose_name = 'Видео ролик'
        verbose_name_plural = 'Видео ролики'
    def __str__(self):
        return self.title

@receiver(pre_delete, sender=Video)
def delete_post_photo(sender, instance, **kwargs):
    """
    Сигнал, вызываемый перед удалением экземпляра Video.
    Удаляет связанный файл видео при удалении записи о видео.
    """
    instance.video_file.delete()

class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_author')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
    def __str__(self):
        return f"Like from {self.author} to {self.video}"

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_author')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_date = models.DateTimeField(blank=False, default=now)

    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'
    def __str__(self):
        return f"Comment from {self.author} to {self.content}"
