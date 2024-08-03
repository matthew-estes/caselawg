from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Case, Task

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def case_index(request):
    cases = Case.objects.all() 
    return render(request, 'cases/case_index.html', {'cases': cases})

def case_detail(request, pk):
    case = Case.objects.get(pk=pk)
    return render(request, "cases/case_detail.html", {'case': case})

def task_index(request):
    tasks = Task.objects.all() 
    return render(request, 'tasks/task_index.html', {'tasks': tasks})

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, "tasks/task_detail.html", {'task': task})

class CaseCreate(CreateView):
    model = Case
    fields = '__all__'
    success_url = '/cases/'

class CaseUpdate(UpdateView):
    model = Case
    fields = ['attorney', 'description', 'case_status', 'case_stage']

class CaseDelete(DeleteView):
    model = Case
    success_url = '/cases/'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = '/task/'

class TaskUpdate(UpdateView):
    model = Case
    fields = ['attorney', 'description', 'case_status', 'case_stage']

class TaskDelete(DeleteView):
    model = Case
    success_url = '/task/'