from apps.videos.models import Video


class VideoServices:
    @staticmethod
    def get_video_models():
        return Video.objects.all()

