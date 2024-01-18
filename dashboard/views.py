from django.shortcuts import render
from accounts.models import MemberProfile,Children,Spouse

# no. of sunday sch children

def no_sch_child(request):
    sunsch = Children.objects.filter(dept='teens').count()
    return render(request,'dashboards/countsundaysch.html',{'sunsch':sunsch})