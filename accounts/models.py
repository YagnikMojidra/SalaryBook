from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Business(models.Model):
    business_name=models.CharField(max_length=60)
    business_address=models.TextField(max_length=150)
    business_mail=models.EmailField(max_length=40)
    business_owner_name=models.CharField(max_length=30)
    business_mobile_number=models.BigIntegerField()

    def __str__(self):
        return self.business_name

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username