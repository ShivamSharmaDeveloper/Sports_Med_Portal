from django.db import models
from django.forms import CharField, EmailField, ModelForm, Textarea

# Create your models here.

class Teachers(models.Model):
    Name = models.CharField(max_length=255)
    Department = models.CharField(max_length=20)
    Email = models.EmailField(max_length=255)
    Password = models.CharField(max_length=255)


class Meta:
    db_table = "teachers"

class Sports(models.Model):
    Name = models.CharField(max_length=100)
    Rollno = models.BigIntegerField() # max_length = 15
    Course = models.CharField(max_length=20)
    Gender = models.CharField(max_length=6)
    Department = models.CharField(max_length=10)
    Phonenumber = models.BigIntegerField()  # max_length=10
    Game = models.CharField(max_length=15)
    Entry = models.CharField(max_length=6)  
    EntryTime = models.DateTimeField(auto_now_add=True)  
    ExitTime = models.DateTimeField(auto_now=True)  


class Meta:
    db_table = "sports"


class Medical(models.Model):
    Name = models.CharField(max_length=100)
    Rollno = models.BigIntegerField()  # max_length=15
    Course = models.CharField(max_length=20)
    Phonenumber = models.BigIntegerField() # max_length=10
    Age = models.IntegerField() # max_length=80
    Email = models.EmailField(max_length=255)
    MaritalStatus = models.CharField(max_length=15)
    Weight = models.IntegerField() # max_length=300
    Height = models.FloatField() # max_length=100
    Gender = models.CharField(max_length=10)
    PatientProblem = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Country = models.CharField(max_length=10)
    City = models.CharField(max_length=10)
    state = models.CharField(max_length=25)
    pincode = models.IntegerField() # max_length=6
    # Entry = models.CharField(max_length=6)
    EntryTime = models.DateTimeField(auto_now_add=True)


class Meta:
    db_table = "medical"
