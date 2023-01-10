from django.db import models
from cloudinary.models import CloudinaryField
from .sitedescription import Sitedescription
from ckeditor.fields import RichTextField

class Siteimage(models.Model):
    site_name=models.ForeignKey(Sitedescription, verbose_name='select Heritage Site', on_delete=models.CASCADE)
    siteimage_name=models.CharField(max_length=500,verbose_name='Image Name')
    siteimage_url=CloudinaryField('Upload Image')
    is_banner_image=models.BooleanField(null=True,default=False)
    siteimage_description= RichTextField(null=True,blank=True)
    create_date=models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.siteimage_name
    