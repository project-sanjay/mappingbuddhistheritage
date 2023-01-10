from django.core import validators
from django import forms
from django.forms import fields


class Form_Change_Login(forms.Form):
    login_name=forms.CharField(label='Username',max_length=50,widget=forms.TextInput(attrs={'class':'form-control back'}))
    login_old_password=forms.CharField(label='Old Password',max_length=20,widget=forms.TextInput(attrs={'class':'form-control back'}))
    login_new_password=forms.CharField(label='New Password',max_length=20,widget=forms.TextInput(attrs={'class':'form-control back'}))
