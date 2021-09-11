from django.db import models

# Create your models here.

class Employee(models.Model):
    empcode = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    mobilenum = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)