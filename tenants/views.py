# Create your views here.

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

import requests
import responses
import json

from .models import *
from .Api import ApiUsers

def getUserIP(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddUser(APIView):
    def post(self, request, format=None):
        request.data['PubIp']=getUserIP(request)
        returnData=ApiUsers.addUser(self,request.data)
        if returnData['RS'] == "SUCCESS":
            return Response(returnData, status=status.HTTP_202_ACCEPTED)
        else:
            print(returnData)
            return Response(returnData, status=status.HTTP_400_BAD_REQUEST)
