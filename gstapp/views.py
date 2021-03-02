from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime

@api_view(['GET'])
def gst(request):
	t= datetime.now()
	msg = "server date & time is " + str(t)
	return Response({'msg':msg})