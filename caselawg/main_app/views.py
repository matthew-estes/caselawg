from django.shortcuts import render
from .models import Case 

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def case_index(request):
    cases = Case.objects.all() 
    return render(request, 'cases/case_index.html', {'cases': cases})

def case_detail(request, case_id):
    case = Case.objects.get(id=case_id)
    return render(request, "cases/case_detail.html", {'case': case})
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