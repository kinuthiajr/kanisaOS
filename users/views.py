from django.shortcuts import render, redirect
from users.forms import RegistrationForm
from users.forms import SigninForm
from django.contrib.auth import login, authenticate,logout,get_user_model
from . models import User
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from typing import Protocol

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('signin')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('homepage')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("users/acc_active_email.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

def register_view(request, **kwargs):
    if request.user.is_authenticated:
        return HttpResponse(f"You're already authenticated as {request.user.email}.")
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.username}")
            user = form.save(commit=False)
            user.is_active = False
            form.save()  
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('home')  
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
            messages.error(request, 'Invalid email or password. Please try again!')
            print(f"Form errors: {form.errors}")
    else:
        form = AuthenticationForm(request)
    return render(request, 'users/signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')
