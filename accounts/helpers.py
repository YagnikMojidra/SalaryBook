from email import message
from django.core.mail import send_mail
from django.conf import settings
from random import *

def send_forget_password_mail(email,token):
    subject="Your Forget Password Link Below:"
    message=f"Hi,Click on the link to reset your password http://127.0.0.1:5502/accounts/changepassword/{token}"
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)
    return True


def send_otp_mail(email,otp):
    subject="Your Login Otp Of SalaryBook Is Below:"
    message=f"Your Login Otp is: {otp}  for SalaryBook."
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)
    return True