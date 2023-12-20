from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
     path('',views.home,name='home'),

  
    #  path('',views.add_user,name='add_user'),
]
   
