from email import message
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.models import *
from accounts.forms import *
from django.views import View
from accounts.helpers import *
from random import *
import re
import uuid
from django.contrib.auth.decorators import login_required
from employees.models import *
from EmpAttandance.models import *

otp=""
# for login page
def login(request):
    pageInfo = {
        'title': 'Login-SalaryBook'
    }
    try:
        if request.method == 'POST':
            username = request.POST.get('user_name')
            password = request.POST.get('password')
            if not username or not password:
                messages.success(
                    request, 'Both Username and Password are required.')
                return redirect('/accounts/login/')
            user_obj = User.objects.filter(username=username).first()
            if user_obj is None:
                messages.success(request, 'User not found.')
                return redirect('/accounts/login/')

            user = authenticate(username=username, password=password)

            if user is None:
                messages.success(request, 'Wrong password.')
                return redirect('/accounts/login/')

            auth.login(request,user)
            global otp
            for i in range(8):
                otp+=str(randint(0,9))
            # print(otp)
            send_otp_mail(user_obj.email , otp)
            return redirect('/accounts/otpverify/')

    except Exception as e:
        print(e)
    return render(request, 'login.html', pageInfo)

# for otp page
@login_required(login_url='/accounts/login/')
def otpverify(request):
    pageInfo = {
        'title': 'Otp-Verify-SalaryBook'
    }
    try:
        if request.method == 'POST':
            
            otp2 = request.POST.get('otp')

            if otp!=otp2:
                messages.success(request,"Invalid Otp Please Try Again.")
                return redirect('/accounts/otpverify/')
            # print("Successfully login")
            return redirect('/accounts/owner/')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'otpverify.html',pageInfo)

# for signup page
def signup(request):
    pageInfo = {
        'title': 'Sign-Up-SalaryBook'
    }
    try:
        if request.method == 'POST':
            username = request.POST.get('user_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password2 = request.POST.get('pwd2')
            pattern=re.compile(r'')
        
        try:
        
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/accounts/signup/')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/accounts/signup/')
            print(len(password))
            # if (len(password)<8):
            #     messages.info(request,"Password length should be 8 character or above.")
            #     return redirect('/accounts/signup/')

            # elif re.search(r'[!@#$%^&]',password) is None:
            #     messages.info(request,"Password Must Contains atleast one special Symbol.")
            #     return redirect('/accounts/signup/')

            # elif re.search(r'\d',password) is None:
            #     messages.info(request,"Password Must Contains atleast one Digit.")
            #     return redirect('/accounts/signup/')

            # elif re.search(r'[A-Z]',password) is None:
            #     messages.info(request,"Password Must Contains atleast one Capital letter.")
            #     return redirect('/accounts/signup/')

            # elif re.match(r'[a-z A-Z 0-9 !@#$%^&]{8}',password):
            #     pattern=re.compile(r'[a-z A-Z 0-9 !@#$%^&]{8}',password)    
            #     result=pattern.match(password)
            #     print(result)
            print("success")
            user_obj = User(username = username , email = email,first_name=first_name, last_name=last_name)
            user_obj.set_password(password2)
            user_obj.save()
    
            profile_obj = Profile.objects.create(user = user_obj )
            profile_obj.save()
            return redirect('/accounts/login/')

        except Exception as e:
            print(e)

    except Exception as e:
            print(e)

    return render(request , 'signup.html',pageInfo)

# for logout
@login_required(login_url='/accounts/login/')
def logout(request):
    auth.logout(request)
    return redirect('/')

# for redirect to owner_dash_board page
@login_required(login_url='/accounts/login/')
def owner(request):
    user = User.objects.all()
    bdetail=Business.objects.all().__len__()
    emp = Employees.objects.all().__len__()
    pageInfo = {
        'title': 'Dashboard-SalaryBook',
        'user': user,
        'emp':emp,
        'bdetail':bdetail
        
    }
    return render(request, 'common_dash_board.html', pageInfo)


# for profile page
@login_required(login_url='/accounts/login/')
def profile(request):
    user = User.objects.all()
    pageInfo = {
        'title': 'User-Profile-SalaryBook',
        'user': user
    }
    return render(request, 'profile.html', pageInfo)

# for reset password
def pwdreset(request):
    pass


# for forget password
def forgetpass(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('user_name')
            
            if not User.objects.filter(username=username).first():
                messages.success(request, 'Not user found with this username.')
                return redirect('/accounts/forgetpassword/')
            
            user_obj = User.objects.get(username = username)
            token = str(uuid.uuid4())
            profile_obj= Profile.objects.get(user = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email , token)
            messages.success(request, 'An email is sent.')
            return redirect('/accounts/forgetpassword/')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'forget_password.html')

# for changepassword
def changepass(request , token):
    context = {}
    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id,
        'title': 'Change-Password-SalaryBook'
        }
        
        if request.method == 'POST':
            new_password = request.POST.get('password1')
            confirm_password = request.POST.get('password2')
            user_id = request.POST.get('user_id')
            
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/accounts/changepassword/{token}/')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/accounts/changepassword/{token}/')
                         
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/accounts/login/')
            
            
            
        
        
    except Exception as e:
        print(e)
    return render(request , 'change_password.html' , context)



# change profile page
class changeProfile(View):
    
    def get(self, request, username):
        user = User.objects.get(username=username)
        fm = ChangeUserProfile(instance=user)
        pageInfo = {
            'title': 'User-Change-Profile-SalaryBook',
            'form': fm
        }
        return render(request, 'changeProfile.html', pageInfo)

    def post(self, request, username):
        user = User.objects.get(username=username)
        fm = ChangeUserProfile(request.POST, instance=user)
        pageInfo = {
            'title': 'User-Change-Profile-SalaryBook',
            'form': fm
        }
        if fm.is_valid():
            fm.save()
            return redirect('/accounts/profile/')

        else:
            return render(request, 'changeProfile.html', pageInfo)


# for business detail pages
# business home page

class Home(View):
    def get(self, request):
        bd_data = Business.objects.all()
        pageInfo = {
            'title': 'Business-Details-SalaryBook',
            'bd_data': bd_data
        }
        return render(request, 'business_details.html', pageInfo)


# add business page

class Add_business(View):
    def get(self, request):
        fm = AddStudentForm()
        pageInfo = {
            'title': 'Add-New-Business-Details-SalaryBook',
            'form': fm
        }
        return render(request, 'add_business_details.html', pageInfo)

    def post(self, request):
        fm = AddStudentForm(request.POST)
        pageInfo = {
            'title': 'Add-New-Business-Details-SalaryBook',
            'form': fm
        }
        if fm.is_valid():
            fm.save()
            return redirect('/accounts/business_details/')
        else:
            return render(request, 'add_business_details.html', pageInfo)


# delete business page

class delete_business(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        bdata = Business.objects.get(id=id)
        bdata.delete()
        return redirect('/accounts/business_details/')


# update business page

class update_business(View):
    def get(self, request, id):
        bdata = Business.objects.get(id=id)
        fm = AddStudentForm(instance=bdata)
        pageInfo = {
            'title': 'Update-Business-Details-SalaryBook',
            'form': fm
        }
        return render(request, 'update_business_details.html', pageInfo)

    def post(self, request, id):
        bdata = Business.objects.get(id=id)
        fm = AddStudentForm(request.POST, instance=bdata)
        pageInfo = {
            'title': 'Update-Business-Details-SalaryBook',
            'form': fm
        }
        if fm.is_valid():
            fm.save()
            return redirect('/accounts/business_details/')
        else:
            return render(request, 'update_business_details.html', pageInfo)
