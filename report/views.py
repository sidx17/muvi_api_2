from django.shortcuts import render

from rest_framework import viewsets
from .models import User,Video
from .serializers import UserSerializer,VideoSerializer


# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VideoView(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer