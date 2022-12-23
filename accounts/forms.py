from django.core import validators
from django import forms
from .models import Business
from django.contrib.auth.models import User


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ("business_name", "business_address", "business_mail",
                  "business_owner_name", "business_mobile_number")
        widgets = {
            'business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'business_address': forms.Textarea(attrs={'class': 'form-control'}),
            'business_mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'business_owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'business_mobile_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ChangeUserProfile(forms.ModelForm):
    class Meta:
        model = User

        fields = ("username", "first_name", "last_name",
                  "email")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control fw-bold'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control fw-bold'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control fw-bold'}),
            'email': forms.EmailInput(attrs={'class': 'form-control fw-bold'}),
        }
