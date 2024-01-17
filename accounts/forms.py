# forms.py
from django import forms
from .models import MemberProfile,Spouse,Children

class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = '__all__'
        

class SpouseForm(forms.ModelForm):
    class Meta:
        model = Spouse
        fields = '__all__'

class ChildrenForm(forms.ModelForm):
    class Meta:
        model = Children
        fields = '__all__'