from rest_framework_simplejwt.tokens import RefreshToken
from apps.user.models import Channel
class GetLoginResponseService:
    @staticmethod
    def get_login_response(user, request):
        refresh = RefreshToken.for_user(user)
        data = {"refresh": str(refresh), "access": str(refresh.access_token)}
        return data

class ChannelService:
    @staticmethod
    def get_channel_class():
        return Channel.objects.all()
