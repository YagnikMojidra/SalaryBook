
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from EmpAttandance.models import *
from EmpAttandance.forms import *
from django.views import View
from employees.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
# for showing employees attandance

class HomeEmployeeAttandance(View):
    def get(self, request):
        e_data = Employees.objects.all()
        a_data = empAttandance.objects.all()
        pageInfo = {
            'title': 'Employees-Attandance-Details-SalaryBook',
            'e_data': e_data,
            'a_data': a_data
        }
        return render(request, 'emp_attan_details.html', pageInfo)


# for adding employees attandance

class AddEmployeeAttandance(View):
    
    def get(self, request):
        fm=AddEmpAttanForm()
        pageInfo = {
            'title': 'Add-Employees-Attandance-SalaryBook',
            'form':fm
        }
        return render(request, 'add_emp_attandance.html', pageInfo)
    
    def post(self, request):
        fm = AddEmpAttanForm(request.POST)
        pageInfo = {
            'title': 'Add-Employees-Attandance-SalaryBook',
            'form': fm
        }
        if fm.is_valid():
            fm.save()
            return redirect('/EmpAttandance/emp_attan_details/')
        else:
            return render(request, 'add_emp_details.html', pageInfo)

# for editing employees attandance data

class EditEmployeeAttandance(View):
    def get(self, request, id):
        edata = empAttandance.objects.get(id=id)
        fm=AddEmpAttanForm(instance=edata)
        pageInfo = {
            'title': 'Edit-employees-Attandance-SalaryBook',
            'form': fm
        }
        return render(request, 'edit_emp_attandance.html', pageInfo)

    def post(self, request, id):
        edata = empAttandance.objects.get(id=id)
        fm=AddEmpAttanForm(request.POST,instance=edata)
        pageInfo = {
            'title': 'Edit-employees-Attandance-SalaryBook',
            'form': fm
        }
        if fm.is_valid():
            fm.save()
            return redirect('/EmpAttandance/emp_attan_details/')
        else:
            return render(request, 'edit_emp_attandance.html', pageInfo)

    
# for Delete employees attandance data

class DeleteEmployeeAttandance(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        bdata = empAttandance.objects.get(id=id)
        bdata.delete()
        return redirect('/EmpAttandance/emp_attan_details/')