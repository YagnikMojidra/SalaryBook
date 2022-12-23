from django.core import validators
from django import forms
from .models import Employees
from .models import *
from datetime import *

class AddEmpForm(forms.ModelForm):
    class Meta:
        model = Employees
        types = (
            ("Per Day Basis", "Per Day Basis"),
        )

        employee_salary_type = forms.ChoiceField(choices=types, required=True)
        employee_attandance_type = forms.ChoiceField(
            choices=types, required=True)

        fields = ("employee_name", "employee_address", "employee_contact_number",
                  "employee_salary_type", "employee_salary", "employee_attandance_type")

        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control fw-bold', 'requiured': True}),
            'employee_address': forms.Textarea(attrs={'class': 'form-control fw-bold', 'requiured': True}),
            'employee_contact_number': forms.NumberInput(attrs={'class': 'form-control fw-bold', 'requiured': True}),
            'employee_salary': forms.NumberInput(attrs={'class': 'form-control fw-bold', 'requiured': True}),

        }


