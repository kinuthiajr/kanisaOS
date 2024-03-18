from django.urls import path
from . import views

urlpatterns = [
    path('workspace/',views.workspace,name='workspace'),
    path('memberform/',views.member,name='memberform')
]
