from django.shortcuts import render, redirect
from users.forms import RegistrationForm,PasswordResetForm,SetPasswordForm
from users.forms import SigninForm
from django.contrib.auth import login, authenticate,logout,get_user_model
from . models import User
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models.query_utils import Q

# email verification for new users
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

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.get(Q(email=user_email))
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("users/template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject,message,to=[associated_user.email])
                if email.send():
                    messages.success(request,
                             """
                        <h2>Password reset sent</h2><hr>
                        <p>
                            We've emailed you instructions for setting your password, if an account exists with the email you entered. 
                            You should receive them shortly.<br>If you don't receive an email, please make sure you've entered the address 
                            you registered with, and check your spam folder.
                        </p>
                        """        
                        )
                else:
                    messages.error(request,"Problem sending reset password email, <b>SERVER PROBLEM</b>")
            return redirect('home')

    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="users/password_reset.html", 
        context={"form": form}
        )

def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        if request.method =='POST':
            form = SetPasswordForm(user,request.POST)
            if form.is_valid():
                user.save()
                messages.success(request, "Your password has been sent. Please go ahead and <b>Signin</b> now. ")
            else:
                messages.error(request,"Problem in sending password")
        form = SetPasswordForm(user)
        return render(request,'users/password_reset_confirm.html',{'form':form})
    else:
        messages.error(request,'Something went wrong')
    return redirect('home')

def signout(request):
    logout(request)
    return redirect('home')
