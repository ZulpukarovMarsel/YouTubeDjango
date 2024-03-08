from rest_framework import serializers
from apps.user.models import *

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'

