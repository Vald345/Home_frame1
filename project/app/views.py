from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world. Bla bla bla bla.")

def index2(request):
    return HttpResponse("Not Hello world. Text Text Text Text Text")

def index3(request):
    return HttpResponse("Home work done")