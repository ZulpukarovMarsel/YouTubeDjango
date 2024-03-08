from rest_framework import serializers
from apps.user.models import *

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SignInSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, help_text="min length 8", min_length=8
    )
