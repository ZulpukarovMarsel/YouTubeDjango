from apps.videos.models import Video, Like, Comment


class VideoServices:
    @staticmethod
    def get_video_models():
        """
        Получаем все объекты Video из базы данных.
        """
        return Video.objects.all()


class LikeServices:
    @staticmethod
    def get_like_models():
        """
        Получаем все объекты Like из базы данных.
        """
        return Like.objects.all()

    @staticmethod
    def get_class_video_like(instance):
        """
        Получаем объекты Like, относящиеся к конкретному видео.
        """
        return Like.objects.filter(video=instance)


class CommentServices:
    @staticmethod
    def get_comment_models():
        """
        Получаем все объекты Comment из базы данных.
        """
        return Comment.objects.all()

    @staticmethod
    def get_class_video_comment(instance):
        """
        Получаем объекты Comment, относящиеся к конкретному видео.
        """
        return Comment.objects.filter(video=instance)
