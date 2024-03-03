from rest_framework import permissions
from rest_framework import generics
from apps.videos.serializers import *
from apps.videos.services import VideoServices, LikeServices, CommentServices

# Create your views here.

class VideoListView(generics.ListCreateAPIView):
    queryset = VideoServices.get_video_models()
    serializer_class = VideosSerializer
    permission_classes = [permissions.IsAuthenticated]

class VideoDetailView(generics.RetrieveAPIView):
    queryset = VideoServices.get_video_models()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

class LikeModelViewSet(generics.ListAPIView):
    queryset = LikeServices.get_like_models()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentModelViewSet(generics.ListAPIView):
    queryset = CommentServices.get_comment_models()
    serializer_class = CommentSerializer
    permission_classes = [permissions]

