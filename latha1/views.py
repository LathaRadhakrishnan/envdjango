from django.shortcuts import render

# Create your views here.
# helloworldapp/views.py

from django.http import HttpResponse
from django.conf import settings

def hello_world(request):
    


    name = settings.NAME
    return HttpResponse(f"Your name is : {name}")
   




