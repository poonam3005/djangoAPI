from .import views
from django.urls import path

urlpatterns = [
    path('employee', views.Employees.as_view()),  
    path('employee/<pk>', views.Employees.as_view()),  
    path('company', views.Companies.as_view()),  
    path('company/<pk>', views.Companies.as_view()), 
]

