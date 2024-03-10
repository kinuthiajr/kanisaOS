from django.shortcuts import render,redirect
from . models import User


# Create your views here.

def home(request):
    """ Landing page"""
    return render(request,'kiongozi/home.html')
