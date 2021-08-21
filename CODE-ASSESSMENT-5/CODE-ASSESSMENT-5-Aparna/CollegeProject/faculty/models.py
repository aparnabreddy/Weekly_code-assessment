from django.db import models

# Create your models here.
class faculty(models.Model):
    faculty_code=models.IntegerField()
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobilenumber=models.BigIntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
