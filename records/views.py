from django.shortcuts import render,redirect
from . forms import MemberProfileForm,SpouseForm,ChildrenForm
from . models import MemberProfile,Spouse,Children
from django.contrib import messages



# Create your views here.
def workspace(request):
    """ Redirects to a navbar after signin or login """
    return render(request,'records/workspace.html')

# MemberProfile views
def member(request):
    if request.method == 'POST':
        print(request.POST)
        member_form = MemberProfileForm(request.POST)
        if member_form.is_valid():
            member_form.save()
            messages.success(request,'Member Successfully submitted')
            return redirect('memberstable')
        else:
            if 'name' in member_form.errors:
                messages.error(request,'Name is required')
            if 'gender' in member_form.errors:
                messages.error(request,'Gender is required')
    else:
        member_form = MemberProfileForm()
    return render(request,'records/memberform.html',{'member_form':member_form})

def member_table(request):
    members = MemberProfile.objects.all()
    return render(request,'records/memberstable.html',{'members':members})