from django.shortcuts import render
from accounts.models import MemberProfile,Children,Spouse

# no. of sunday sch children

def no_sch_child(request):
    sunsch = MemberProfile.objects.filter(cell_group='jerusalem').count()
    return render(request,'dashboards/countsundaysch.html',{'sunsch':sunsch})