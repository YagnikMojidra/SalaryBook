from email import message
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from employees.models import *
from employees.forms import *
from django.views import View
from django.contrib.auth.decorators import login_required
from EmpAttandance.models import *

# Create your views here.
# for Employees detail pages

# Employees home page


class Home(View):
    def get(self, request):
        e_data = Employees.objects.all()
        pageInfo = {
            'title': 'Employees-Details-SalaryBook',
            'e_data': e_data
        }
        return render(request, 'emp_details.html', pageInfo)

# add employee page


class Add_emp(View):
    def get(self, request):
        fm = AddEmpForm()
        pageInfo = {
            'title': 'Add-New-Employees-Details-SalaryBook',
            'form': fm
        }
        return render(request, 'add_emp_details.html', pageInfo)

    def post(self, request):
        fm = AddEmpForm(request.POST)
        pageInfo = {
            'title': 'Add-New-Employees-Details-SalaryBook',
            'form': fm
        }
        if fm.is_valid():
            fm.save()
            return redirect('/employees/emp_details/')
        else:
            return render(request, 'add_emp_details.html', pageInfo)


# update employee page
class update_emp(View):
    def get(self, request, id):
        bdata = Employees.objects.get(id=id)
        fm = AddEmpForm(instance=bdata)
        pageInfo = {
            'title': 'Update-Employees-Details-SalaryBook',
            'form': fm
        }
        return render(request, 'update_emp_details.html', pageInfo)

    def post(self, request, id):
        bdata = Employees.objects.get(id=id)
        fm = AddEmpForm(request.POST, instance=bdata)
        pageInfo = {
            'title': 'Update-Employees-Details-SalaryBook',
            'form': fm
        }
        if fm.is_valid():
            fm.save()
            return redirect('/employees/emp_details/')
        else:
            return render(request, 'update_emp_details.html', pageInfo)


# delete employee page
class delete_emp(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        bdata = Employees.objects.get(id=id)
        bdata.delete()
        return redirect('/employees/emp_details/')


# for employee salary page
class HomeEmployeeSalary(View):
    def get(self, request):

        e_data = Employees.objects.all()
        atandata = empAttandance.objects.all()
        # for getting withdraw amount
        record = dict()
        for a in e_data:
            for b in atandata:
                if a.employee_name == b.employee_name:
                    if a.employee_name in record.keys():
                        li = record[a.employee_name]
                        li[1] += b.withdraw_amount
                        record[a.employee_name] = li
                    else:
                        record[a.employee_name] = list(
                            [a.employee_name, b.withdraw_amount, b.types, a.employee_salary])
        # print(record)

        # for getting attandance data
        reAttan = dict()
        for a in e_data:
            for b in atandata:
                if a.employee_name == b.employee_name:            
                    if a.employee_name in reAttan.keys():
                        if b.types == "Absent":
                            reAttan[a.employee_name].append(0)
                        elif b.types == "Present":
                            reAttan[a.employee_name].append(1)
                        elif b.types == "Half Present":
                            reAttan[a.employee_name].append(0.5)
                    else:
                        reAttan[a.employee_name] = list([1 if b.types == "Present" else 0.5 if b.types == "Half Present" else 0])                
        
        reAttan= {key: [sum(values)] for key, values in reAttan.items()}

        # for merge count attandance
        res = {key: value + reAttan[key] for key, value in record.items()}       
        # print(res)

        # for  adding total salary values
        res3={key: [value[3]*value[4]] for key, value in res.items()}
        res = {key: value + res3[key] for key, value in res.items()}

        # for net salary
        res4={key: [value[5]-value[1]] for key, value in res.items()}
        res = {key: value + res4[key] for key, value in res.items()}
        print(res)


        pageInfo = {
            'title': 'Employees-Salary-Details-SalaryBook',
            'e_data': e_data,
            'record': res,
        }

        return render(request, 'emp_salary_details.html', pageInfo)
