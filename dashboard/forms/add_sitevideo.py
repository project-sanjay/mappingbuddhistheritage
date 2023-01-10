from django.core import validators
from django import forms
from django.forms import fields
from dashboard.models.sitevideo import Sitevideo

class Form_Add_Sitevideo(forms.ModelForm):
    class Meta:
        model=Sitevideo
        fields=['site_name','sitevideo_name','sitevideo_url',]
        widgets={
            'site_name':forms.Select(attrs={'class':'form-control back'}),
            'sitevideo_name':forms.TextInput(attrs={'class':'form-control back'}),
            'sitevideo_url':forms.URLInput(attrs={'class':'form-control back'}),
        }
