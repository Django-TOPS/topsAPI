from urllib import response
from django.shortcuts import render
from .models import studInfo
from .serializers import studSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import requests



def index(request):
    url="http://127.0.0.1:8000/getstudall/"
    req=requests.get(url)
    data=req.json()
    print(data)
    return render(request,'index.html',{'data':data})


@api_view(['GET'])
def getstudall(request):
    if request.method=='GET':
        studObj=studInfo.objects.all()
        studSerial=studSerializers(studObj,many=True)
        return Response(studSerial.data)

@api_view(['GET','PUT'])
def getstud(request,pk):
    try:
        studobj=studInfo.objects.get(id=pk)
    except studInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        studserial=studSerializers(studobj)
        return Response(studserial.data)
    elif request.method=="PUT":
        studserial=studSerializers(studobj,data=request.data)
        if studserial.is_valid():
            studserial.save()
            return Response(studserial.data)
        return Response(studserial.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def createstud(request):
    if request.method=='POST':
        studSerial=studSerializers(data=request.data)
        if studSerial.is_valid():
            studSerial.save()
            return Response(studSerial.data,status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def deletestud(request,pk):
    if request.method=='DELETE':
        try:

            studid=studInfo.objects.get(id=pk)
            studInfo.delete(studid)
            return Response("Record Deleted!")
        except studInfo.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


