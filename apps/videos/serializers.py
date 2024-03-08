from rest_framework import serializers
from apps.videos.models import *
from apps.user.serializers import ChannelSerializer


class VideosSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer(read_only=True)
    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'video_file', 'channel', 'created_date')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
