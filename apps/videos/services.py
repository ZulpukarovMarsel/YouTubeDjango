from apps.videos.models import Video, Like, Comment


class VideoServices:
    @staticmethod
    def get_video_models():
        return Video.objects.all()


class LikeServices:
    @staticmethod
    def get_like_models():
        return Like.objects.all()

    @staticmethod
    def get_class_video_like(instance):
        return Like.objects.filter(video=instance)


class CommentServices:
    @staticmethod
    def get_comment_models():
        return Comment.objects.all()

    @staticmethod
    def get_class_video_comment(instance):
        return Comment.objects.filter(video=instance)
