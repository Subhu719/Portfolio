from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login,logout, authenticate
# Create your models here.
class contact(models.Model):
     name =models.CharField(max_length=255)
     subject =models.CharField(max_length=225, default="-", null=True)
     email=models.EmailField()
     msg=models.CharField(max_length=255)
     def __str__(self):
        return self.name



class Portfolio(models.Model):

    CATEGORY_CHOICES = [
        ('app', 'Web App'),
        ('product', 'Frontend'),
        ('branding', 'Backend'),
        ('books', 'UI Design'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    image = models.ImageField(upload_to='media')
    live_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class category(models.Model):
    name=models.CharField(max_length=255, default='portfolio')
    
    def __str__(self):
        return self.name   
   
   