from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path("about/", views.about, name="about"),
    path('case/create', views.CaseCreate.as_view(), name='case-create'),
    path('case/<int:pk>/update', views.CaseUpdate.as_view(), name='case-update'),
    path('case/<int:pk>/delete', views.CaseDelete.as_view(), name='case-delete'),
    path('cases/', views.case_index, name='case_index'),
    path('cases/<int:case_id>/', views.case_detail, name='case_detail'),
]