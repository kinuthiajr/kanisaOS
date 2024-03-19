from django.urls import path
from . import views

urlpatterns = [
    path('workspace/',views.workspace,name='workspace'),
    path('memberform/',views.member,name='memberform'),
    path('memberstable/',views.member_table,name='memberstable'),
    path('update/<int:record_id>/',views.edit,name='update'),
]
