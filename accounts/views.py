from django.shortcuts import render,redirect,get_object_or_404
from .forms import MemberProfileForm,SpouseForm,ChildrenForm
from .models import *



# Create your views here.
def home_screen(request):
    return render(request, 'accounts/home.html')

def spouse(request):
    if request.method == 'POST':
        spouse_form = SpouseForm(request.POST)
        if spouse_form.is_valid():
            spouse_form.save()
            return redirect('spousedata')  
        else:
            print(spouse_form.errors)  
    else:
        spouse_form = SpouseForm()

    return render(request, 'accounts/spouse.html', {'spouse_form': spouse_form})


def member(request):

    if request.method == 'POST':
        member_form =MemberProfileForm(request.POST)
        if member_form.is_valid():
            member_form.save()
            return redirect('memberdata')
        else:
            print(member_form.errors)
    else:
        member_form = MemberProfileForm()
        
    return render(request,'accounts/member.html',{'member_form':member_form})


def tabular(request):
    members = MemberProfile.objects.all()
    return render(request,'accounts/memberdata.html',{'members':members})

def spousetabular(request):
    spouse = Spouse.objects.all()
    return render(request,'accounts/spousedata.html',{'spouse':spouse})


def edit(request, record_id):
    record = get_object_or_404(MemberProfile, pk=record_id)
    member_form = MemberProfileForm(instance=record)

    if request.method == 'POST':
        member_form = MemberProfileForm(request.POST, instance=record)
        if member_form.is_valid():
            member_form.save()
            return redirect('memberdata')
    return render(request, 'accounts/edit.html', {'member_form': member_form, 'record': record})


def deletemember(request,record_id):
    record = get_object_or_404(MemberProfile,pk=record_id)
    member_form = MemberProfileForm(instance=record)
    if request.method =='POST':
        record.delete()
        return redirect('memberdata')
    return render(request, 'accounts/delete.html', {'record': record,'member_form':member_form})


def editspouse(request,record_id): 
    
    record = get_object_or_404(Spouse,pk=record_id)
    spouse_form = SpouseForm(instance=record)
    if request.method == 'POST':
        spouse_form = SpouseForm(request.POST,instance=record)
        if spouse_form.is_valid():
            spouse_form.save()
            return redirect('spousedata')
    return render(request,'accounts/editspouse.html',{'spouse_form':spouse_form,'record':record})

def listmembers(request):
    queryset = MemberProfile.objects.all()
    return render(request,'accounts/memberdata.html',{'queryset':queryset})

def listspouse(request):
    queryset = Spouse.objects.all()
    return render(request,'accounts/spousedata.html',{'queryset':queryset})

def deletespouse(request,record_id):
    record = get_object_or_404(Spouse,pk=record_id)
    spouse_form = SpouseForm(instance=record)
    if request.method == 'POST':
        record.delete()
        return redirect('spousedata')
    return render(request,'accounts/deletespouse.html',{'record':record,'spouse_form':spouse_form})

# Child views

def child(request):
    if request.method =='POST':
        child_form = ChildrenForm(request.POST)
        if child_form.is_valid():
            child_form.save()
            return redirect('home')
        else:
            print(child_form.errors)
    else:
        child_form = ChildrenForm()
    return render(request,'accounts/child.html',{'child_form':child_form})
