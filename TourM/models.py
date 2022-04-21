from audioop import reverse
from django.db import models
from django.urls import reverse

# Create your models here.

class Provinces(models.Model):
    Provinces = models.CharField(max_length=255)

    def __str__(self):
        return self.Provinces     
    def get_absolute_url(self):
        return reverse('homeView')

    

class comments(models.Model):
    comments = models.CharField(default='',max_length=255)
    def __str__(self):
        return self.comments 

    
    def get_absolute_url(self):
        return reverse('homeView')



class Post(models.Model):
    title = models.CharField(max_length=255)
    creator =models.CharField(default='The company',max_length=255 )  
    body = models.TextField()
    days = models.CharField(max_length=2)
    price = models.CharField(default='',max_length=8)
    Provinces = models.CharField(default='',max_length=255)
    pack_img = models.ImageField(null = True, blank=True, upload_to="pacImages/")
   


    def __str__(self):
        return self.title + ' | '+ str(self.creator)

    
    def get_absolute_url(self):
        return reverse('homeView')


   