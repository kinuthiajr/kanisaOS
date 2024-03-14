from django.shortcuts import render

# Create your views here.
def workspace(request):
    return render(request,'records/workspace.html')