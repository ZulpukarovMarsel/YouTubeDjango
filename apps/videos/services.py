from apps.videos.models import Video, Like, Comment


class VideoService:
    @staticmethod
    def get_video_class():
        """
        Получаем все объекты Video из базы данных.
        """
        return Video.objects.all()


class LikeService:
    @staticmethod
    def get_like_class():
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


class CommentService:
    @staticmethod
    def get_comment_class():
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
