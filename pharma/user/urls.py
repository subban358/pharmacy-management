from django.urls import path
from . import views
from django.shortcuts import render, redirect

urlpatterns = [
	path('',views.home, name='home'),
	path('login', views.login, name = 'login'),
	path('signup', views.signup, name = 'signup'),
	path('logout', views.logout, name = 'logout'),	
]