from django.db import models
from .sitedescription import Sitedescription
from embed_video.fields import EmbedVideoField

class Sitevideo(models.Model):
    site_name=models.ForeignKey(Sitedescription, verbose_name='select Heritage Site', on_delete=models.CASCADE)
    sitevideo_name=models.CharField(max_length=500,verbose_name='Video Name')
    sitevideo_url=EmbedVideoField(blank=True)
    create_date=models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.sitevideo_name