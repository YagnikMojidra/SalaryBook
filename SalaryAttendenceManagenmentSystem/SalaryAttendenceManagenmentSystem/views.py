from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# for home page
def home(request):
    pageInfo = {
        'title': 'Home-SalaryBook'
    }
    return render(request, 'index.html', pageInfo)

# for aboutus page
def aboutUs(request):
    pageInfo = {
        'title': 'AboutUs-SalaryBook'
    }
    return render(request, 'aboutus.html', pageInfo)

# for privacy-policy page
def privacy(request):
    pageInfo = {
        'title': 'Privacy-Policy-SalaryBook'
    }
    return render(request, 'privacy.html', pageInfo)

# for term and conditions page
def tAndc(request):
    pageInfo = {
        'title': 'Terms-And-Conditions-SalaryBook'
    }
    return render(request, 'termsandcondition.html')




