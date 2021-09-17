from django.db import models

# Create your models here.
class Admin(models.Model):
    adminname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)


class Donor(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    bgroup=models.CharField(max_length=50)
    mobilenumber=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
  