from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    #return HttpResponse("Hey!! This is my first Http Response")
    return render(request , "index.html")

def success_page(request):
    return HttpResponse("This is Success Page")