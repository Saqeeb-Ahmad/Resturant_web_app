from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class authentication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True)
    
class AboutItems(models.Model):
    allimage = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    title_desc = models.TextField()
    
class About_ourstory(models.Model):
    ourstory_desc = models.TextField()
    
class ServicesItem_desc(models.Model):
    title_desc = models.TextField()
    
    
class ServicesItem(models.Model):
    allimage = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    
    
class Feedback_from(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,  null=True)
    feedback = models.TextField()
    rating = models.TextField()
