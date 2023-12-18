from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    #return HttpResponse("Hey!! This is my first Http Response")
    peoples = [
        {'name' : 'Abhi' , 'age' : 30},
        {'name' : 'Jay' , 'age' : 20},
        {'name' : 'Rey' , 'age' : 10}
    ]
    
    
    return render(request , "index.html", context = {'Page ': 'Django' , 'peoples':peoples})

def about(request):
    context = { "Page" : "about"}
    return render(request, "about.html" , context)

def contact(request):
    co = { "Page" : "contact"}
    return render(request, "contact.html" , co)