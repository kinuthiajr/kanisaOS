from . models import MemberProfile,Spouse,Children
from django import forms

# Validation is done at the Form level

# Member profile form
class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = ['name','phone','baptism_date','confirmation_date','spouse','gender','marital_status','service_attends','communicant','department','cell_group']

    # Form validation of the requird fields
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            return forms.ValidationError('Name is requird')
        return name

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            return forms.ValidationError('Gender is required')
        return gender       

# spouse form
class SpouseForm(forms.ModelForm):
    class Meta:
        model = Spouse
        fields = ['name', 'phone', 'baptism_date', 'confirmation_date', 'marital_status', 'gender', 'service_attends', 'communicant', 'cell_group','department']

    # Form validation of the required fields
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            return forms.ValidationError('Name is requird')
        return name

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            return forms.ValidationError('Gender is required')
        return gender


# children form 
    
class ChildrenForm(forms.ModelForm):
    class Meta:
        model = Children
        fields = ['parent','name','date_of_birth','confirmation_date','baptism_date','department','gender','communicant']

    # Form validation of the required fields
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            return forms.ValidationError('Name is requird')
        return name

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            return forms.ValidationError('Gender is required')
        return gender
        