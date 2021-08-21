from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    admission_number=models.IntegerField()
    roll_number=models.IntegerField()
    college=models.CharField(max_length=50)
    parent_name=models.CharField(max_length=50)
