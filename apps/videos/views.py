from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from apps.videos.serializers import *
from apps.videos.services import VideoServices, LikeServices, CommentServices

# Create your views here.

class VideoModelViewSet(ModelViewSet):
    queryset = VideoServices.get_video_models()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]


class LikeModelViewSet(ModelViewSet):
    queryset = LikeServices.get_like_models()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentModelViewSet(ModelViewSet):
    queryset = CommentServices.get_comment_models()
    serializer_class = CommentSerializer
    permission_classes = [permissions]
