from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path("about/", views.about, name="about"),
    path('cases/', views.case_index, name='case-index'),
    path('cases/<int:pk>/', views.case_detail, name='case-detail'),
    path('case/create/', views.CaseCreate.as_view(), name='case-create'),
    path('case/<int:pk>/update/', views.CaseUpdate.as_view(), name='case-update'),
    path('case/<int:pk>/close/', views.CaseUpdate.as_view(), name='case-close'),
    path('case/<int:pk>/delete/', views.CaseDelete.as_view(), name='case-delete'),
    path('task/create/', views.TaskCreate.as_view(), name='task-create'),
    path('tasks/', views.task_index, name='task-index'),
    path('tasks/', views.task_detail, name='task-detail'),
   path('task/<int:pk>/update/', views.TaskUpdate.as_view(), name='task-update'),
   path('task/<int:pk>/close/', views.TaskUpdate.as_view(), name='task-close'),
    path('task/<int:pk>/delete/', views.TaskDelete.as_view(), name='task-delete'),
]