from rest_framework import serializers
from apps.videos.models import *

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
