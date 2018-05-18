from rest_framework import serializers
from .models import User,Video


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name')


class VideoSerializer(serializers.ModelSerializer):
    #user_details = UserSerializer(source="user_id" ,read_only=True)
    class Meta:
        model = Video
        fields = ('watch_duration','bandwidth_usage')

