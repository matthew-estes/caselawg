from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from .models import Case, Task
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.urls import reverse
from django.utils import timezone


class Home(LoginView):
    template_name = "home.html"


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("case-index")
        else:
            error_message = "Invalid sign up - try again"

    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)


def about(request):
    return render(request, "about.html")


@login_required
def case_index(request):
    cases = Case.objects.filter(user=request.user)
    return render(request, "cases/case_index.html", {"cases": cases})


@login_required
def case_detail(request, pk):
    case = Case.objects.get(pk=pk)
    tasks = Task.objects.filter(case=case)
    cases = Case.objects.filter(user=request.user)
    return render(
        request,
        "cases/case_detail.html",
        {"case": case, "cases": cases, "tasks": tasks},
    )


@login_required
def task_index(request):
    tasks = Task.objects.all()
    cases = Case.objects.filter(user=request.user)
    return render(request, "tasks/task_index.html", {"tasks": tasks, "cases": cases})


@login_required
def task_index2(request):
    tasks = Task.objects.all()
    cases = Case.objects.filter(user=request.user)
    return render(request, "tasks/task_index2.html", {"tasks": tasks, "cases": cases})


@login_required
def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    cases = Case.objects.filter(user=request.user)
    return render(request, "tasks/task_detail.html", {"task": task, "cases": cases})


def tasksDataAPI(request):
    data = Task.objects.all()
    dataList = []

    for i in data:
        dataList.append(
            {
                "task_name": i.task_name,
                "task_type": i.task_type,
                "task_status": i.task_status,
                "task_description": i.task_description,
                "estimated_time": i.estimated_time,
                "actual_time": i.actual_time,
                "id": i.task_id,
            }
        )

    return JsonResponse(dataList, safe=False)


class CaseCreate(LoginRequiredMixin, CreateView):
    model = Case

    fields = [
        "name",
        "client",
        "date_opened",
        "date_closed",
        "description",
        "case_status",
        "case_stage",
    ]
    success_url = "/cases/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        return redirect(reverse("case-detail", kwargs={"pk": self.object.pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cases"] = Case.objects.filter(user=self.request.user)
        context["form_title"] = "Create Case"
        return context


class CaseUpdate(LoginRequiredMixin, UpdateView):
    model = Case
    fields = ["client", "description", "case_status", "case_stage"]

    def get_success_url(self):
        return reverse("case-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cases"] = Case.objects.filter(user=self.request.user)
        return context


class CaseCloseView(View):
    def get(self, request, pk):
        case = Case.objects.get(pk=pk)
        case.case_status = "C"
        case.date_closed = timezone.now() 
        case.save()
        return redirect("case-detail", pk=pk)


class CaseDelete(LoginRequiredMixin, DeleteView):
    model = Case
    success_url = "/cases/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cases"] = Case.objects.filter(user=self.request.user)
        return context

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['task_name', 'task_type', 'task_status', 'task_description', 'date_created', 'estimated_time', 'actual_time']  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
        context["form_title"] = "Create Task"
        context["case"] = Case.objects.get(pk=self.kwargs["pk"])
        context["cases"] = Case.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.case = Case.objects.get(pk=self.kwargs["pk"]) 
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('case-detail', kwargs={'pk': self.kwargs["pk"]})


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['task_name', 'task_type', 'task_status', 'task_description', 'date_created', 'date_closed', 'estimated_time', 'actual_time'] 

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        task = self.object
        case = task.case
        return redirect(reverse("case-detail", kwargs={"pk": case.pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
        context["cases"] = Case.objects.filter(user=self.request.user)
        return context


class TaskCloseView(LoginRequiredMixin, UpdateView):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        case = task.case
        task.task_status = "C"
        task.date_closed = timezone.now() 
        task.save()
        return redirect("case-detail", pk=case.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cases"] = Case.objects.filter(user=self.request.user)
        return context


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/cases'

    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        case = task.case
        task.delete()
        return redirect("case-detail", pk=case.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cases"] = Case.objects.filter(user=self.request.user)
        return context