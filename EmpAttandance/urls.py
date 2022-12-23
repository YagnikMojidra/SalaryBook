from django.contrib import admin
from django.urls import path
from EmpAttandance import views
from .views import *
from django.contrib.auth.decorators import login_required


# url patterns
urlpatterns = [
    path("emp_attan_details/",login_required(HomeEmployeeAttandance.as_view()),name="emp_attan_details"),
    path("add_emp_attan_details/",login_required(AddEmployeeAttandance.as_view()),name="add_emp_attan_details"),
    path("edit_emp_attan_details/<int:id>/",login_required(EditEmployeeAttandance.as_view()),name="edit_emp_attan_details"),
    path("delete_emp_attan_details/",login_required(DeleteEmployeeAttandance.as_view()),name="delete_emp_attan_details"),
    
]