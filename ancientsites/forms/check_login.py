from django.core import validators
from django import forms
from django.forms import fields
from ancientsites.models.login import Login

class Form_Add_Login(forms.ModelForm):
    class Meta:
        model=Login
        fields=['login_name','login_password',]
        widgets={
            'login_name':forms.TextInput(attrs={'class':'form-control back'}),
            'login_password':forms.PasswordInput(attrs={'class':'form-control back'}),
        }
