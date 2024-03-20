from django.urls import path
from . import views

urlpatterns = [
    path('workspace/',views.workspace,name='workspace'),
    path('memberform/',views.member,name='memberform'),
    path('memberstable/',views.member_table,name='memberstable'),
    path('memberupdate/<int:record_id>/',views.member_edit,name='memberupdate'),
    path('memberdelete/<int:record_id>/',views.member_erase,name='memberdelete'),
    path('spouseform/',views.spouse,name='spouseform'),
    path('spousetable/',views.spouse_table,name='spousetable'),
    path('spouseupdate/<int:record_id>/',views.spouse_edit,name='spouseupdate'),

]
