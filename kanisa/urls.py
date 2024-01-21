"""kanisa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from dashboard.views import (
    dashboard,
)
from accounts.views import (
    home_screen,
    spouse,
    member,
    tabular,
    edit,
    deletemember,
    editspouse,
    spousetabular,
    listmembers,
    listspouse,
    deletespouse,
    child,
    MemberProfileChildview,
    editchild,
    deletechild,
    listchild,
   
)
from users.views import(
    register_view,
    sign_in,
    signout,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen, name='home'),
    path('users/',register_view,name='users'),
    path('signin/',sign_in,name='signin'),
    path('spouse/',spouse,name='spouse'),
    path('member/',member,name='member'),
    path('memberdata/',tabular,name='memberdata'),
    path('spousedata/',spousetabular,name='spousedata'),
    path('edit/<int:record_id>/',edit,name='edit'),
    path('delete/<int:record_id>/',deletemember,name='delete'),
    path('editspouse/<int:record_id>/',editspouse,name='editspouse'),
    path('memberdata/',listmembers,name='memberdata'),
    path('spousedata/',listspouse,name='spousedata'),
    path('deletespouse/<int:record_id>/',deletespouse,name='deletespouse'),
    path('signout/',signout,name='signout'),
    path('child/',child,name='child'),
    path('memberdetails/<int:pk>/',MemberProfileChildview.as_view(),name='memberdetails'),
    path('editchild/<int:record_id>/',editchild,name='editchild'),
    path('deletechild/<int:record_id>/',deletechild,name='deletechild'),
    path('childrendata/',listchild,name='childrendata'),
    # dashboard
    path('dashboard/',dashboard,name='dashboard'),
    
] 
