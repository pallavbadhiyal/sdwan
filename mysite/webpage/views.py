from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello! This is a Django webpage created with Python.</h1>")