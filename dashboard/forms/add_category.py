from django.core import validators
from django import forms
from django.forms import fields
from dashboard.models.category import Category

class Form_Add_Category(forms.ModelForm):
    class Meta:
        model=Category
        fields=['category_name','category_image',]
        widgets={
            'category_name':forms.TextInput(attrs={'class':'form-control back'}),
        }
