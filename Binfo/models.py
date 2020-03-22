from django.db import models

# Create your models here.
class Blood(models.Model):
    First_Name=models.CharField(max_length=30)
    Last_Name=models.CharField(max_length=30)
    DOB=models.DateField()
    BloodGroup=models.CharField(max_length=5)
    Phone=models.CharField(max_length=10)
    City=models.CharField(max_length=30)
