from django.shortcuts import render, redirect
from users.forms import RegistrationForm
from users.forms import SigninForm
from django.contrib.auth import login, authenticate,logout
from . models import User
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def register_view(request, **kwargs):
    if request.user.is_authenticated:
        return HttpResponse(f"You're already authenticated as {request.user.email}.")
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(request,email=email, password=raw_password)

            if account is not None:
                login(request, account)  

                destination = kwargs.get('next')
                if destination:
                    return redirect(destination)
                return redirect('member')  
    else:
        form = RegistrationForm()

    context = {'registration_form': form}
    return render(request, 'users/users.html', context)



def sign_in(request, **kwargs):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            print(f"User variable after authenticate: {user}")
            
            if user:
                login(request, user)
                messages.success(request,'Login Successful')
                print("User logged in successfully.")
                return redirect('member')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            print(f"Form errors: {form.errors}")
    
    else:
        form = AuthenticationForm(request)

    return render(request, 'users/signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')
