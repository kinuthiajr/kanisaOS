from django.shortcuts import render,redirect,get_object_or_404
from .forms import MemberProfileForm,SpouseForm
from .models import *



# Create your views here.
def home_screen(request):
    return render(request, 'accounts/home.html')

def spouse(request):
    if request.method == 'POST':
        spouse_form = SpouseForm(request.POST)
        if spouse_form.is_valid():
            spouse_form.save()
            return redirect('home')  
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
    
