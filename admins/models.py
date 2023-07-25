from django.db import models

# Create your models here.
class Admins(models.Model):
    username= models.CharField(max_length=200, unique=True) 
    password= models.CharField(max_length=200) 
    name = models.CharField(max_length=200) 
    email= models.EmailField(max_length=254, unique=True)
    contact = models.CharField(max_length=13,unique=True)
    address = models.TextField()
    

class Employee(models.Model):
    username= models.CharField(max_length=200, unique=True) 
    password= models.CharField(max_length=200) 
    name = models.CharField(max_length=200) 
    email= models.EmailField(max_length=254, unique=True)
    contact = models.CharField(max_length=13,unique=True)
    address = models.TextField()