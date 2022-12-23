from django.contrib import admin
from django.urls import path
from accounts import views
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('',accounts)
    path("login/", views.login, name="login"),
    path("otpverify/", views.otpverify, name="otpverify"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("owner/", views.owner, name="owner"),
    path("profile/", views.profile, name="profile"),
    
    path("password_reset/",views.pwdreset,name="password reset"),
    path("forgetpassword/",views.forgetpass,name="Forget password"),
    path("changepassword/<token>/",views.changepass,name="change password"),
    
    path("change_profile/<str:username>/",
         login_required(changeProfile.as_view()), name="ChangeProfile"),
    path("business_details/", login_required(Home.as_view()), name="business_details"),
    path("add_business_details/", login_required(Add_business.as_view()),
         name="add_business_details"),
    path("delete_business_details/", login_required(delete_business.as_view()),
         name="delete_business_details"),
    path("update_business_details/<int:id>/",
         login_required(update_business.as_view()), name="update_business_details"),
    

]
