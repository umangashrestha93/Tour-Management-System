from audioop import reverse
from django.db import models
from django.contrib.auth.models  import User
from django.urls import reverse

# Create your models here.

class Provinces(models.Model):
    Provinces = models.CharField(max_length=255)

    def __str__(self):
        return self.Provinces 

    
    def get_absolute_url(self):
        return reverse('homeView')



class Post(models.Model):
    title = models.CharField(max_length=255)
    creator =models.CharField(default='The company',max_length=255 )  #deletes all the posts made by the admin which was deleted.
    body = models.TextField()
    days = models.CharField(max_length=2)
    price = models.CharField(default='',max_length=8)
    Provinces = models.CharField(default='',max_length=255)
    


    def __str__(self):
        return self.title + ' | '+ str(self.creator)

    
    def get_absolute_url(self):
        return reverse('homeView')


   