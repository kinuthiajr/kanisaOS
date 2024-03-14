from django.urls import path
from . import views

urlpatterns = [
    path('workspace/',views.workspace,name='workspace'),
]
