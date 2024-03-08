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

