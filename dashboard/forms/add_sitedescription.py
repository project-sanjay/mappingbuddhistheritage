from django.core import validators
from django import forms
from django.forms import fields, widgets
from dashboard.models.sitedescription import Sitedescription
class Form_Add_Sitedescription(forms.ModelForm):
    class Meta:
       model=Sitedescription
       fields=['state_name','category_name','site_name','site_also_name','site_latitude','site_longitude','site_description',]
       widgets={
            'site_name':forms.TextInput(attrs={'class':'form-control back'}),
            'site_also_name':forms.TextInput(attrs={'class':'form-control back'}),
            'site_latitude':forms.NumberInput(attrs={'class':'form-control back'}),
            'site_longitude':forms.NumberInput(attrs={'class':'form-control back'}),
            'category_name':forms.Select(attrs={'class':'form-control back' }),
            'state_name':forms.Select(attrs={'class':'form-control back' }),
            'site_description':forms.Textarea(attrs={'class':'form-control back' }),
       }