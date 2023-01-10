from django.core import validators
from django import forms
from django.forms import fields
from dashboard.models.country import Country

class Form_Add_Country(forms.ModelForm):
    class Meta:
        model=Country
        fields=['country_name',]
        widgets={
            'country_name':forms.TextInput(attrs={'class':'form-control back','id':'country_name'}),
        }
