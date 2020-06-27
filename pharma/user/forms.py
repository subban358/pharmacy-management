from django import forms
from django.core import validators
from .models import patientsPersonalDetail, Medicine, Order, DoctorDetail, Rating, Report

class DateInput(forms.DateInput):
    	input_type = 'date'

class patient_personalDetailForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = patientsPersonalDetail
        fields = ['user', 'dob', 'address', 'mobile']
        widgets = {
            'dob': DateInput(attrs={'class': 'form-control required'}),
            'mobile' : forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Please enter your mobile number'
            }),
            'address' : forms.Textarea(attrs={
                'class': 'form-control required',
                'placeholder': 'Enter your address here'
            }),
            'user' : forms.Select(attrs={'class': 'form-control required'})
        }

class OrderForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Order
        fields = ('medicine', 'quantity')
        widgets = {
            'medicine': forms.Select(attrs={
                'class': 'form-control'
            }),
            'quantity' : forms.NumberInput(attrs={'class': 'form-control'}),
        }

class DoctorDetailForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = DoctorDetail
        fields = '__all__'
        labels = {
            'DoctorName' : "Name",
            'DoctorEmail' : "Email Id",
            'DoctorPassword' : "Password",
        }
        
        widgets = {
            'DoctorName' : forms.TextInput(attrs={'class': 'form-control'}),
            'DoctorEmail' : forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Please Enter Your Email Address'
                }),
            'DoctorPassword' : forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Please Enter Your Password'
            }),
            'Specialization' : forms.TextInput(attrs={'class': 'form-control'})    
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['doctor', 'rating']
        labels = {
            'doctor' : 'Doctor',
            'rating' : 'Rating'
        }
        widgets = {
            'doctor' : forms.Select(attrs={'class': 'form-control'}),
            'rating' : forms.NumberInput(attrs={'class': 'form-control'})
        }
class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['height', 'weight', 'blood_grp']       
        labels = {
            'height': 'Height',
            'weight': 'Weight',
            'blood_grp': 'Blood Group'
        } 
        widgets = {
            'height':  forms.NumberInput(attrs={'step': 0.5, 'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'blood_grp': forms.TextInput(attrs={'class': 'form-control'})
        }