from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def reciepes(request):
    return render (request , "recipies.html")