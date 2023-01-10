from django.core import validators
from django import forms
from django.forms import fields
from dashboard.models.state import State

class Form_Add_State(forms.ModelForm):
    class Meta:
        model=State
        fields=['state_name','country_name',]
        widgets={
            'state_name':forms.TextInput(attrs={'class':'form-control back','id':'state_name'}),
            'country_name':forms.Select(attrs={'class':'form-control back','id':'country_name_select'}),
        }
