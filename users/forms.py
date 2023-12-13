from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from users.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required. Add a valid Email')
    
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Email {email} already exists.')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Username {username} is in use.')
        return username

class SigninForm(AuthenticationForm):
    username = forms.EmailField(
        max_length= 255,
        widget=forms.TextInput(attrs={'autofocus':True})
    )