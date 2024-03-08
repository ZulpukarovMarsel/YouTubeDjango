from rest_framework import serializers
from apps.user.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "image", "firstname", "lastname", "email")

class ChannelSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    subscribers = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Channel
        fields = ("id", "image", "name", "description", "owner", "subscribers", "created_date")

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("image", "firstname", "lastname", "email", "password")

class SignInSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, help_text="min length 8", min_length=8
    )

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()