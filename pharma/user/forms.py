from django import forms
from django.core import validators
from .models import patientsPersonalDetail, Medicine

class DateInput(forms.DateInput):
    	input_type = 'date'

class patient_personalDetailForm(forms.ModelForm):
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

class MedicineForm(forms.ModelForm):
    model = Medicine
    fields = ['med_name', 'med_brand', 'med_stock', 'med_price', 'med_type']
    widgets = {
        'med_name': forms.TextInput(attrs={
            'class': 'form-control'
        })
    }
