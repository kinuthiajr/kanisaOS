from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import MemberProfileForm,SpouseForm,ChildrenForm
from django.views.generic import DetailView
from .models import *



# Create your views here.
def home_screen(request):
    return render(request, 'accounts/home.html')

def spouse(request):
    if request.method == 'POST':
        spouse_form = SpouseForm(request.POST)
        if spouse_form.is_valid():
            if 'name' in request.POST and request.POST['name'] != 'None':
                spouse_form.save()
                messages.success(request,'Spouse successfully Submitted!',extra_tags='spouse')
                return redirect('spousedata')  
            else:
                messages.error(request,'Spouse name is required')  
    else:
        spouse_form = SpouseForm()
    return render(request, 'accounts/spouse.html', {'spouse_form': spouse_form})

def member(request):
    if request.method == 'POST':
        member_form =MemberProfileForm(request.POST)
        if member_form.is_valid():
            if 'name' in request.POST and request.POST['name'] != 'None':
                member_form.save()
                messages.success(request,'Member Successfully Submitted!',extra_tags='member')
                return redirect('memberdata')
            else:
                messages.error(request," Member name is required",)
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
            messages.success(request,'Sucessfully Edited Member!',extra_tags='edit')
            member_form.save()
            return redirect('memberdata')
    return render(request, 'accounts/edit.html', {'member_form': member_form, 'record': record})


def deletemember(request,record_id):
    record = get_object_or_404(MemberProfile,pk=record_id)
    member_form = MemberProfileForm(instance=record)
    if request.method =='POST':
        record.delete()
        messages.success(request,'Member Deleted!',extra_tags='deletemember')
        return redirect('memberdata')
    return render(request, 'accounts/delete.html', {'record': record,'member_form':member_form})


def editspouse(request,record_id): 
    record = get_object_or_404(Spouse,pk=record_id)
    spouse_form = SpouseForm(instance=record)
    if request.method == 'POST':
        spouse_form = SpouseForm(request.POST,instance=record)
        if spouse_form.is_valid():
            spouse_form.save()
            messages.success(request,'Successfully Edited Spouse!',extra_tags='editspouse')
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
        messages.success(request,'Spouse Deleted!',extra_tags='deletespouse')
        return redirect('spousedata')
    return render(request,'accounts/deletespouse.html',{'record':record,'spouse_form':spouse_form})


class MemberProfileChildview(DetailView):
    """class-based view for member profile to show: children/spouse/all details of a church member"""
    model = MemberProfile
    template_name = 'accounts/memberdetails.html'
    context_object_name = 'member'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        member = self.get_object()
        children = member.children.all()
        context['children'] = children
        return context


# Child views
def child(request):
    if request.method =='POST':
        child_form = ChildrenForm(request.POST)
        if child_form.is_valid():
            child_form.save()
            messages.success(request, "Child has been successfully added.",extra_tags='child')
            return redirect('childrendata')
        else:
            messages.error(request, "Parent/Member profile is required")
    else:
        child_form = ChildrenForm()
    return render(request,'accounts/child.html',{'child_form':child_form})


def editchild(request,record_id):
    record = get_object_or_404(Children,pk=record_id)
    child_form = ChildrenForm(instance=record)
    if request.method =='POST':
        child_form = ChildrenForm(request.POST,instance=record)
        if child_form.is_valid():
            child_form.save()
            messages.success(request,'Successfully Edited Child!',extra_tags='editchild')
            return redirect('childrendata')
    return render(request,'accounts/editchild.html',{'record':record,'child_form':child_form})

def deletechild(request,record_id):
    record = get_object_or_404(Children,pk=record_id)
    child_form = ChildrenForm(instance=record)
    if request.method == 'POST':
        record.delete()
        messages.success(request,'Child Deleted!',extra_tags='deletechild')
        return redirect('childrendata')
    return render(request,'accounts/deletechild.html',{'child_form':child_form,'record':record})

def listchild(request):
    children= Children.objects.all()
    return render(request,'accounts/childrendata.html',{'children':children})