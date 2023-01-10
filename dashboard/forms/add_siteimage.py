from django.core import validators
from django import forms
from django.forms import fields, widgets
from dashboard.models.siteimage import Siteimage

class Form_Add_Siteimage(forms.ModelForm):
    class Meta:
       model=Siteimage
       fields=['site_name','siteimage_name','siteimage_url','siteimage_description',]
       widgets={
            'site_name':forms.Select(attrs={'class':'form-control back'}),
            'siteimage_name':forms.TextInput(attrs={'class':'form-control back'}),
            'siteimage_description':forms.Textarea(attrs={'class':'form-control back'}),
       }