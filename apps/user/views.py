from datetime import timezone
from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework import generics, permissions, status, response, exceptions
from django.contrib.auth import authenticate, hashers
from apps.user.models import User
from .serializers import *
from .services import GetLoginResponseService
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