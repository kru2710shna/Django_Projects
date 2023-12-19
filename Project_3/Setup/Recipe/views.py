from django.shortcuts import render
from .models import *
# Create your views here.
def recipe(request):
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
    
        Recipe.objects.create(
            recipe_image = recipe_image,
            recipe_description=recipe_description,
            recipe_name = recipe_name
        )
        
    return render(request , "recipt.html")
 