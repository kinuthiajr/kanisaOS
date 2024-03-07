from django.shortcuts import render

# Create your views here.

def home(request):
    """ Landing page"""
    return render(request,'kiongozi/index.html')

#signup new user
def signup(request):
    return render(request,'kiongozi/signup.html')