from django.contrib import admin
from apps.videos.models import Video, Comment, Like
# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        "id", "title", "description", "video_file", "channel", "created_date")
    search_fields = ("title", "channel", "created_date")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "video", "author", "content", "created_date")
    search_fields = ("video", "author", "created_date")

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "video", "author")
    search_fields = ("video", "author")
