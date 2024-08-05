from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from .models import Case, Task
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginView):
    template_name = 'home.html'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('case-index')
        else:
            error_message = 'Invalid sign up - try again'
    
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def about(request):
    return render(request, "about.html")

@login_required
def case_index(request):
    cases = Case.objects.filter(user=request.user)
    return render(request, "cases/case_index.html", {"cases": cases})

@login_required
def case_detail(request, pk):
    case = Case.objects.get(pk=pk)
    cases = Case.objects.all()
    return render(request, "cases/case_detail.html", {"case": case, "cases": cases})

@login_required
def task_index(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_index.html", {"tasks": tasks})
  
@login_required
def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task})
  

class CaseCreate(LoginRequiredMixin, CreateView):
    model = Case
    fields = "__all__"
    success_url = "/cases/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cases"] = Case.objects.all()
        context["form_title"] = "Create Case"
        return context


class CaseUpdate(LoginRequiredMixin, UpdateView):
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


class CaseDelete(LoginRequiredMixin, DeleteView):
    model = Case
    success_url = "/cases/"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = '/tasks/'
    

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/task/'

