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
	path('buy_med', views.buy_med, name="buy_med"),
	path('bill/<int:oid>', views.bill, name = 'bill'),
	path('doctor', views.doctor, name = 'doctor'),
	path('doctorLogin', views.doctorLogin, name = 'doctorLogin'),
	path('ratedoc', views.ratedoc, name = 'ratedoc'),
	path('book', views.book, name = 'book'),
	path('confirm/<int:Did>', views.confirm, name = 'confirm'),
	path('report/<int:Did>/<int:Pid>', views.report, name = 'report'),
	path('showReport', views.showReport, name ="showReport")
]