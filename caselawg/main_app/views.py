from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Case

class CaseCreate(CreateView):
    model = Case
    fields = '__all__'

class CaseUpdate(UpdateView):
    model = Case
    fields = ['attorney', 'description', 'case_status', 'case_stage']

class CaseDelete(DeleteView):
    model = Case
    success_url = '/cases/'

def home(request):
    return HttpResponse('hello world')

def about(request):
    return HttpResponse("<h1>Caselawg</h1>")

