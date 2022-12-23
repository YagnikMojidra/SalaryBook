from .models import *
from django import forms
from employees.models import *
from django.forms.widgets import *
from employees.models import *

class AddEmpAttanForm(forms.ModelForm):
    class Meta:
        emp=Employees.objects.all().values()
        emp2=[(l['employee_name'],l['employee_name'])for l in emp]
        model=empAttandance
        employee_name=forms.ChoiceField(choices=emp2, required=True)
        date=forms.DateField(input_formats=['%y-%m-%d'])
        withdraw_amount=forms.IntegerField(required=True)
        date=forms.DateField(required=True)
        fields = ("employee_name", "withdraw_amount", "attendance_date",
                  "types")