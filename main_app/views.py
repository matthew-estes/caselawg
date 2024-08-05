from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from .models import Case, Task


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def case_index(request):
    cases = Case.objects.all()
    return render(request, "cases/case_index.html", {"cases": cases})


def case_detail(request, pk):
    case = Case.objects.get(pk=pk)
    cases = Case.objects.all()
    return render(request, "cases/case_detail.html", {"case": case, "cases": cases})


def task_index(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_index.html", {"tasks": tasks})
  

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task})
  

class CaseCreate(CreateView):
    model = Case
    fields = "__all__"
    success_url = "/cases/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cases"] = Case.objects.all()
        context["form_title"] = "Create Case"
        return context


class CaseUpdate(UpdateView):
    model = Case
    fields = ["attorney", "description", "case_status", "case_stage"]
    success_url = '/cases/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cases'] = Case.objects.all() 
        return context


class CaseCloseView(View):
    def get(self, request, pk):
        case = Case.objects.get(pk=pk)
        case.case_status = "C"
        case.save()
        return redirect("case-detail", pk=pk)


class CaseDelete(DeleteView):
    model = Case
    success_url = "/cases/"


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = '/tasks/'
    

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    

class TaskDelete(DeleteView):
    model = Task
    success_url = '/task/'

