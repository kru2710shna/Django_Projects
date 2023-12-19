from django.db import models
from django.shortcuts import render, redirect
# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length = 100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipe_photos')
    
     