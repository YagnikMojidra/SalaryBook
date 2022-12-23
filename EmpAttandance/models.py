from django.db import models
from employees.models import *

# Create your models here.
class empAttandance(models.Model):
    emp=Employees.objects.all().values()
    emp2=[(l['employee_name'],l['employee_name'])for l in emp]
    employee_name=models.CharField(max_length=100,choices=emp2)
    withdraw_amount = models.BigIntegerField()
    attendance_date = models.DateField()
    date_updated = models.DateTimeField(auto_now=True)
    types = models.CharField(max_length=100, choices=[(
        'Absent', 'Absent'), ('Half Present', 'Half Present'), ('Present', 'Present'), ('Tardy', 'Tardy')])
    
    def __str__(self):
        return str(self.employee_name)