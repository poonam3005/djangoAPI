from . import views
from django.urls import path
from api.view.employee import Employees
from api.view.company import Companies
from api.view.department import Departments


urlpatterns = [
    path("employee", Employees.as_view()),
    path("employee/<pk>", Employees.as_view()),
    path("company", Companies.as_view()),
    # path("company/<pk>", Companies.as_view()),
    path("department", Departments.as_view()),
    path("department/<pk>", Departments.as_view()),
]
