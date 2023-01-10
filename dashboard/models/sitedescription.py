from django.db import models
from .category import Category
from .state import State
from ckeditor.fields import RichTextField

class Sitedescription(models.Model):
    site_name=models.CharField(max_length=500,verbose_name='Site Name')
    site_also_name=models.CharField(max_length=500,verbose_name='Also Name As')
    site_latitude=models.FloatField(("Latitude"))
    site_longitude=models.FloatField(("Lognitude"))
    category_name=models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,verbose_name='Select Category')
    state_name=models.ForeignKey(State, on_delete=models.SET_NULL,null=True,verbose_name='Select State')
    site_description= RichTextField(null=True,blank=True)
    create_date=models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.site_name
    
        