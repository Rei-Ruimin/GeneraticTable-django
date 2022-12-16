from dataclasses import fields
from django import forms
from .models import QuinnEmployee, DelayCode
from django.forms.widgets import DateInput # need to import

class QuinnEmployeeForm(forms.ModelForm):
    class Meta:
        model = QuinnEmployee
        fields = '__all__'
        widgets = {
            'original_start_date': DateInput(attrs={'type': 'date'}),
            'termination_date': DateInput(attrs={'type': 'date'})
        }

class DelayCodeForm(forms.ModelForm):
    class Meta:
        model = DelayCode
        fields = '__all__'
    
