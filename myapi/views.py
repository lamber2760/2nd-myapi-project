from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def firstapi(request):
    return Response({
        "Message":"this is my first get api",
        "data":"this is all data"
    })