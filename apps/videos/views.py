from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from apps.videos.serializers import *
from apps.videos.models import Video
from apps.videos.services import VideoServices

# Create your views here.

class VideoModelViewSet(ModelViewSet):
    queryset = VideoServices.get_video_models()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]


