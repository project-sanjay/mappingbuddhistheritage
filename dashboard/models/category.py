from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    category_name=models.CharField(max_length=200)
    category_image = CloudinaryField('image')
    create_date=models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.category_name
    