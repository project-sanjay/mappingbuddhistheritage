from django.db import models
from .country import Country

class State(models.Model):
    state_name=models.CharField(max_length=200)
    country_name=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True,verbose_name='Select Country')
    create_date=models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.state_name
    