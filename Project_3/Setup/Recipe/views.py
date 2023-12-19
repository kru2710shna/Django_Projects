from django.shortcuts import render

# Create your views here.
def recipt(request):
    return render(request , "recipt.html")
