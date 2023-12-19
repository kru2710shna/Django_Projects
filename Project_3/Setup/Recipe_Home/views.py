from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    
    peoples = [
        {'name' : 'Abhi' , 'age' : 27},
        {'name' : 'Jay' , 'age' : 7},
        {'name' : 'Meet' , 'age' : 60}
    ]
    
    return render(request , "index.html", context = { 'page' : 'Django App' , 'peoples': peoples})

def contact(request):
    context = {'page' : 'Contact'} 
    return render(request , "contact.html")

def about(request):
    context = {'page' : 'About'}
    return render(request , "about.html" , context)