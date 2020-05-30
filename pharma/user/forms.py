from django import forms
from django.core import validators
from .models import patientsPersonalDetail

class DateInput(forms.DateInput):
    	input_type = 'date'

class patient_personalDetailForm(forms.ModelForm):
    class Meta:
        model = patientsPersonalDetail
        fields = ['user', 'dob', 'address', 'mobile']
        widgets = {
            'dob': DateInput()
        }
