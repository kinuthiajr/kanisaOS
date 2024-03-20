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

def member_edit(request,record_id):
    """" Populates a form with the data from the database to update it """
    record = get_object_or_404(MemberProfile,pk=record_id)
    member_form = MemberProfileForm(instance=record)
    if request.method == 'POST':
        member_form = MemberProfileForm(request.POST,instance=record)
        if member_form.is_valid():
            member_form.save()
            messages.success(request,'Successfully updated member')
            return redirect('memberstable')
    return render(request,'records/memberupdate.html',{'record':record,'member_form':member_form})


def member_erase(request,record_id):
    """ Discards a record """
    record = get_object_or_404(MemberProfile,pk=record_id)
    member_form = MemberProfileForm(instance=record)
    if request.method == 'POST':
        member_form = MemberProfileForm(request.POST,instance=record)
        if member_form.is_valid():
            record.delete()
            messages.success(request,'Successfully deleted member')
            return redirect('memberstable')
    return render(request,'records/memberdelete.html',{'record':record,'member_form':member_form})


    # Spouse Views

def spouse(request):
    if request.method =="POST":
        print(request.method)
        spouse_form = SpouseForm(request.POST)
        if spouse_form.is_valid():
            spouse_form.save()
            messages.success(request,'Spouse suceessfully submitted')
            return redirect('spousetable')
        else:
            if 'name' in spouse_form.errors:
                messages.error(request,'Name is required')
            if 'gender' in spouse_form.errors:
                messages.error(request,'Gender is required')
    else:
        spouse_form = SpouseForm()
    return render(request,'records/spouseform.html',{'spouse_form':spouse_form})


def spouse_table(request):
    spouses = Spouse.objects.all()
    return render(request,'records/spousetable.html',{'spouses':spouses})


def spouse_edit(request,record_id):
    """ Populates spouse data to a form so for editing """
    record = get_object_or_404(Spouse,pk=record_id)
    spouse_form = SpouseForm(instance=record)
    if request.method == 'POST':
        spouse_form = SpouseForm(request.POST,instance=record)
        if spouse_form.is_valid():
            spouse_form.save()
            messages.success(request,'Successfully edited spouse')
            return redirect('spousetable')
    return render(request,'records/spouseupdate.html',{'record':record,'spouse_form':spouse_form})


def spouse_erase(request,record_id):
    """ Delete a record from the spouse table """
    record = get_object_or_404(Spouse,pk=record_id)
    spouse_form = SpouseForm(instance=record)
    if request.method == 'POST':
        spouse_form = SpouseForm(request.POST,instance=record)
        if spouse_form.is_valid():
            record.delete()
            messages.success(request,'Successfully deleted spouse')
            return redirect('spousetable')
    return render(request,'records/spousedelete.html',{'record':record,'spouse_form':spouse_form})