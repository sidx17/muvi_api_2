from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User,Video
from .serializers import UserSerializer,VideoSerializer
from django.http import HttpResponse,JsonResponse




@api_view(['GET'])
def history(request,id):
    if request.method == 'GET':
        #queryset = Video.objects.filter(user_id=id)
        #serializer = VideoSerializer(queryset, many=True)
        queryset=User.objects.get(pk=id)
        serializer=UserSerializer(queryset)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def watch(request,id):
    if request.method == 'GET':
        userset=User.objects.get(pk=id)
        userSerial=UserSerializer(userset)
        userData=userSerial.data
        #userResponse=JsonResponse(userSerial.data,safe=False)

        videoset = Video.objects.filter(user_id=id)
        videoSerial = VideoSerializer(videoset, many=True )
        videoData=videoSerial.data
        #videoResponse= JsonResponse(videoSerial.data, safe=False)

        for item in videoData:
            item.update(userData)

        myResponse=JsonResponse(videoData,safe=False)


        return myResponse

