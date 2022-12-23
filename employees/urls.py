from django.contrib import admin
from django.urls import path
from employees import views
from .views import *
from django.contrib.auth.decorators import login_required

# url patterns
urlpatterns = [
    path("emp_details/",login_required(Home.as_view()),name="emp_details"),
    path("add_emp_details/",login_required(Add_emp.as_view()),name="add_emp_details"),   
    path("delete_emp_details/",login_required(delete_emp.as_view()),name="delete_emp_details"),   
    path("update_emp_details/<int:id>/",login_required(update_emp.as_view()),name="update_emp_details"),
    path("emp_salary_details/",login_required(HomeEmployeeSalary.as_view()),name="emp_salary_details"),
]