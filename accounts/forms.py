# forms.py
from django import forms
from .models import MemberProfile,Spouse

class MemberProfileForm(forms.ModelForm):
    # Additional MemberProfile fields (add more as needed)
    class Meta:
        model = MemberProfile
        fields = '__all__'

class SpouseForm(forms.ModelForm):
    class Meta:
        model = Spouse
        fields = '__all__'