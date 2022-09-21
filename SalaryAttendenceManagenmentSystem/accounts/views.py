from email import message
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from accounts.models import *

# Create your views here.

# for login page
def login(request):
    pageInfo = {
        'title': 'Login-SalaryBook'
    }
    if request.method == 'POST':
        username = request.POST['user_name']
        passwd = request.POST['password']
        user = auth.authenticate(username=username, password=passwd)

        if user is not None:
            auth.login(request, user)
            return redirect("owner")

        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login")

    else:
        return render(request, 'login.html', pageInfo)

# for signup page
def signup(request):

    pageInfo = {
        'title': 'Sign-Up-SalaryBook'
    }

    if request.method == 'POST':

        # for getting value from the form and store in the variable
        email = request.POST['email']
        password = request.POST['pwd']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['user_name']
        password2 = request.POST['pwd2']

        # for auth we create a user
        if password == password2:
            # for checking username is  alreday exists
            if User.objects.filter(username=username).exists():
                messages.error(
                    request, "UserName is already taken by another user.")
                return redirect('signup')

            # for checking email is  alreday exists
            elif User.objects.filter(email=email).exists():
                messages.error(request, "This Email is already used.")
                return redirect('signup')

            # otherwise do it
            else:
                user = User.objects.create_user(
                    email=email, password=password, first_name=first_name, last_name=last_name, username=username)
                user.save()
                messages.success(request, "User created sucessfully.")
                return redirect('login')
        else:
            messages.warning(request, "Password not matching")
        return redirect('signup')

    # otherwise do it
    else:
        return render(request, 'signup.html', pageInfo)

# for logout
def logout(request):
    auth.logout(request)
    return redirect('/')

# for redirect to owner_dash_board page
def owner(request):
    pageInfo = {
        'title': 'Dashboard-SalaryBook'
    }
    return render(request, 'common_dash_board.html', pageInfo)

# for business detail pages
def bdetails(request):
    business = Business.objects.all()

    pageInfo = {
        'title': 'Business-Info-SalaryBook',
        'busin': business,
    }
    return render(request, 'business_details.html', pageInfo)

# for adding new business
def bdetailsadd(request):

    if request.method == 'POST':
        bname = request.POST['bname']
        bemail = request.POST['bemail']
        baddress = request.POST['baddress']
        bphone = request.POST['bphone']
        bownname = request.POST['bownname']

        busine = Business(
            business_name=bname,
            business_address=baddress,
            business_mail=bemail,
            business_owner_name=bownname,
            business_mobile_number=bphone,
        )
        busine.save()
        return redirect('business_details')

    return render(request, 'business_details.html')

# for editing business details
def bdetailEdit(request):
    
    busine=Business.objects.all()
    pageInfo = {
        'title': 'Business-Details-Edit-SalaryBook',
        'busino': busine,
    }
    return redirect(request, 'business_details', pageInfo)

# for deleting business
def bdDelete(request, id):
    # pass
    busine = get_object_or_404(Business,id=id)
    
    if request.method=="POST":
        busine.delete()
        return redirect(request,'business_details')

    pageInfo = {
        'title': 'Business-Details-Delete-SalaryBook',
        'busin': busine,
    }

    return redirect(request, 'business_details', pageInfo)
