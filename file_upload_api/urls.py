from django.urls import path, re_path
from .views import *



urlpatterns = [
    path('usercreation_api/', CreateUser.as_view(), name='CreateUser'),
    
]