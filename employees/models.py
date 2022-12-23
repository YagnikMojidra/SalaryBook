from datetime import *
from django.db import models
from datetime import *
# Create your models here.


class Employees(models.Model):
    types = (
            ("Per Day Basis", "Per Day Basis"),

    )
    employee_name = models.CharField(max_length=60)
    employee_contact_number = models.BigIntegerField()
    employee_address = models.TextField(max_length=150)
    employee_salary = models.BigIntegerField()
    employee_salary_type = models.CharField(max_length=50, choices=types)
    employee_attandance_type = models.CharField(max_length=50, choices=types)
    employee_attandance_count = models.BigIntegerField()
    employee_total_amount = models.BigIntegerField()
    employee_net_amount = models.BigIntegerField()

    def __str__(self):
        return str(self.employee_name)

