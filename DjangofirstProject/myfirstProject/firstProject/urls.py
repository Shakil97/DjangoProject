from django.conf.urls import url
from firstProject import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    
    path('',views.help,name='help'),
]