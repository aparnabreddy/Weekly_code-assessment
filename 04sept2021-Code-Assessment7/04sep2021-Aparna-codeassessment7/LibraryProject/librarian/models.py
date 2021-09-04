from django.db import models

# Create your models here.
class Librarian(models.Model):
   
    librarian_code=models.IntegerField()
    name=models.CharField(max_length=150)
    address=models.CharField(max_length=120)
    mobile_no=models.BigIntegerField()
    pincode=models.IntegerField()
    email_id=models.CharField(max_length=150)
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=8)
