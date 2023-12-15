from django.urls import path
from . import views

# Url Configuration 
urlpatterns = [
    path('hello/' , views.hello)
]
