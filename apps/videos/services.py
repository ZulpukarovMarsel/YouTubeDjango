from apps.videos.models import Video, Like


class VideoServices:
    @staticmethod
    def get_video_models():
        return Video.objects.all()


class LikeServices:

    @staticmethod
    def get_like_models():
        return Like.objects.all()

