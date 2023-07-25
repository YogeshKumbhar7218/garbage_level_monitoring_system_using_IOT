from django.db import models

# Create your models here.
class User(models.Model):
    username= models.CharField(max_length=200, unique=True) 
    password= models.CharField(max_length=200) 
    name = models.CharField(max_length=200) 
    email= models.EmailField(max_length=254, unique=True)
    contact = models.CharField(max_length=13)
    address = models.TextField()

class Feedback(models.Model):
    feedback = models.TextField()
    username= models.CharField(max_length=200) 
    name = models.CharField(max_length=200) 
    time = models.DateTimeField(null=True, blank=True)
    photo = models.ImageField(upload_to="feedback_image",default="")


