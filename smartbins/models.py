from django.db import models

# Create your models here.
class Smartbin(models.Model):
    bin_number = models.SmallIntegerField(unique=True)
    dry_filled = models.SmallIntegerField(null=True)
    wet_filled = models.SmallIntegerField(null=True)
    location = models.TextField()
    height = models.SmallIntegerField()
    under_employee = models.SmallIntegerField()
    map_location = models.TextField(null=True)
    name = models.CharField(max_length=200,null=True) 
    status = models.CharField(max_length=10,null=True,default="empty") 
    date = models.DateTimeField(null=True, blank=True)
    h_a_m_sent = models.CharField(max_length=10,null=True,default="not")

