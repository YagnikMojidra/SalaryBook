from django.db import models

# Create your models here.
class Business(models.Model):
    business_name=models.CharField(max_length=60)
    business_address=models.TextField(max_length=150)
    business_mail=models.EmailField(max_length=40)
    business_owner_name=models.CharField(max_length=30)
    business_mobile_number=models.BigIntegerField()