from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('hello world')

def about(request):
    return HttpResponse("<h1>Caselawg</h1>")