from django.shortcuts import render,redirect,get_object_or_404
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
    """ Gets all the objects and presents them as a table """
    members = MemberProfile.objects.all()
    return render(request,'records/memberstable.html',{'members':members})

def edit(request,record_id):
    """" Populates a form with the data from the database to update it """
    record = get_object_or_404(MemberProfile,pk=record_id)
    member_form = MemberProfileForm(instance=record)
    if request.method == 'POST':
        member_form = MemberProfileForm(request.POST,instance=record)
        if member_form.is_valid():
            member_form.save()
            messages.success(request,'Successfully updated member')
            return redirect('memberstable')
    return render(request,'records/update.html',{'record':record,'member_form':member_form})