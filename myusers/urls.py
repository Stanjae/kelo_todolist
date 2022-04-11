from re import template
from django.contrib import admin
from django.urls import path
from myusers import views
from django.contrib.auth import views as auth_views
from myusers import forms

urlpatterns = [
    path('signup/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='myusers/login.html'), name='login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='myusers/logout.html'), name='logout'),
    
]
