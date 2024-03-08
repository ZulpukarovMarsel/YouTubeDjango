from datetime import timezone
from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework import generics, permissions, status, response, exceptions
from django.contrib.auth import authenticate, hashers
from apps.user.models import User
from .serializers import *
from .services import GetLoginResponseService, ChannelService
from rest_framework_simplejwt.tokens import RefreshToken

class SignUpAPIView(generics.CreateAPIView):
    # API для регистрации

    serializer_class = SignUpSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                user = User.objects.create_user(
                                                       email=serializer.validated_data["email"],
                                                       password=serializer.validated_data["password"],
                                                       )
                return response.Response(data=GetLoginResponseService.get_login_response(user, request))

            else:
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return response.Response(
                data={"detail": "Пользователь с данной электронной почтой существует!",
                      "status": status.HTTP_409_CONFLICT})


class SignInAPIView(generics.CreateAPIView):
    # API для входа

    serializer_class = SignInSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)
        if not user:
            raise exceptions.AuthenticationFailed

        return response.Response(
            data=GetLoginResponseService.get_login_response(user, request)
        )

class LogoutAPIView(generics.CreateAPIView):
    # API  для выхода

    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            token = RefreshToken(serializer.validated_data['refresh'])
            token.blacklist()
            return response.Response(data={"detail": "Успешно!", "status": status.HTTP_200_OK})
        except Exception as e:
            return response.Response(data={"error": f"{e}"}, status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset


class ChannelView(generics.ListCreateAPIView):
    queryset = ChannelService.get_channel_class()
    serializer_class = ChannelSerializer
    permission_classes = [permissions.IsAuthenticated]

