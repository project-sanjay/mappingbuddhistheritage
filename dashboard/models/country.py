from django.db import models

class Country(models.Model):
    country_name=models.CharField(max_length=200,unique=True)
    create_date=models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.country_name
    