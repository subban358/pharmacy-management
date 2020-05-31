from django.urls import path
from . import views
from django.shortcuts import render, redirect


urlpatterns = [
	path('',views.home, name='home'),
	path('dashboard', views.dashboard, name = 'dashboard'),
	path('patient_personalDetails', views.patient_personalDetails,name='patient_personalDetails'),
	path('login', views.login, name = 'login'),
	path('signup', views.signup, name = 'signup'),
	path('logout', views.logout, name = 'logout'),
	path('edit', views.edit, name="edit"),
]