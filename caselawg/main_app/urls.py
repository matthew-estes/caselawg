from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path("about/", views.about, name="about"),
    path('cases/', views.case_index, name='case_index'),
    path('cases/int:case_id/',views.case_detail, name='case_detail'),
]