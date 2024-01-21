from django.shortcuts import render
from django.db.models import Count
from accounts.models import MemberProfile,Children,Spouse


def dashboard(request):
    """View function that calculates total members/spouse/children based on cell grps,departments and gender respectively"""

    cell_grp_member = MemberProfile.objects.values('cell_group').annotate(total=Count('cell_group'))
    cell_grp_spouse = Spouse.objects.values('cell_group').annotate(total=Count('cell_group'))

    cell_grp_agg = {}
    for member_cell in cell_grp_member:
        cell_grp_agg[member_cell['cell_group']] = cell_grp_agg.get(member_cell['cell_group'],0) + member_cell['total']
    for spouse_cell in cell_grp_spouse:
        cell_grp_agg[spouse_cell['cell_group']] = cell_grp_agg.get(spouse_cell['cell_group'],0) + spouse_cell['total']
    
    gender_member = MemberProfile.objects.values('gender').annotate(total=Count('gender'))
    gender_spouse = Spouse.objects.values('gender').annotate(total=Count('gender'))

    gender_count = {}
    for gender in gender_member:
        gender_count[gender['gender']] = gender_count.get(gender['gender'],0)+gender['total']
    for gender in gender_spouse:
        gender_count[gender['gender']] = gender_count.get(gender['gender'],0)+gender['total']

    dept_member = MemberProfile.objects.values('department').annotate(total=Count('department'))
    dept_spouse = Spouse.objects.values('department').annotate(total=Count('department'))
    
    dept_count = {}
    for dept in dept_member:
        dept_count[dept['department']] = dept_count.get(dept['department'],0)+dept['total']
    for dept in dept_spouse:
        dept_count[dept['department']] = dept_count.get(dept['department'],0)+dept['total']
    
    child_dept = Children.objects.values('dept').annotate(total=Count('dept'))
    child_gender = Children.objects.values('gender').annotate(total=Count('gender'))

    child_count = {}
    for child in child_dept:
        child_count[child['dept']] = child_count.get(child['dept'],0)+child['total']
    for child in child_gender:
        child_count[child['gender']] = child_count.get(child['gender'],0)+child['total']
    
    context = {'cell_grp_agg':cell_grp_agg,
               'gender_count':gender_count,
               'dept_count':dept_count,
               'child_count':child_count,
               }
    
    return render(request,'dashboards/dashboard.html',context)