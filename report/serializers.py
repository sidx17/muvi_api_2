from rest_framework import serializers
from .models import User,Video

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','url','name','email','address')

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ('id','url', 'user_id','watch_duration','bandwidth_usage')
