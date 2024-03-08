from rest_framework import permissions, status
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.videos.serializers import *
from apps.videos.services import VideoServices, LikeServices, CommentServices


class VideoListView(generics.ListCreateAPIView):
    queryset = VideoServices.get_video_models()
    serializer_class = VideosSerializer
    permission_classes = [permissions.IsAuthenticated]

class VideoDetailView(generics.RetrieveAPIView):
    # queryset = VideoServices.get_video_models()
    serializer_class = VideosSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Video, pk=self.kwargs['pk'])

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            video_serializer = self.get_serializer(instance)
            comment_queryset = CommentServices.get_class_video_comment(instance)
            comment_serializer = CommentSerializer(comment_queryset, many=True)
            like_queryset = LikeServices.get_class_video_like(instance)
            like_serializer = LikeSerializer(like_queryset, many=True)

            data = {
                'video': video_serializer.data,
                'likes': like_serializer.data,
                'comments': comment_serializer.data,
            }
            return Response(data, status=status.HTTP_200_OK)
        except VideoServices.get_video_models().DoesNotExist:
            return Response({"error": " Видео не найдено"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"Не удалось получить сведения о видео. {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LikeModelViewSet(generics.ListCreateAPIView):
    queryset = LikeServices.get_like_models()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentModelViewSet(generics.ListCreateAPIView):
    queryset = CommentServices.get_comment_models()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


