from django.contrib import admin
from django.urls import path
from accounts import views
# from django.contrib.auth import views

urlpatterns = [
    # path('',accounts)
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("signup/",views.signup,name="signup"),
    path("owner/",views.owner,name="owner"),
    path("business_details/",views.bdetails,name="business_details"),
    path("business_details/add/",views.bdetailsadd,name="business_details_add"),
    path("business_details/delete/<str:id>/",views.bdDelete,name="business_details_delete"),
    path("business_details/editbd/",views.bdetailEdit,name="business_details_edit"),
      
]


