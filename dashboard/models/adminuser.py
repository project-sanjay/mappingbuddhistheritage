from django.db import models


class Adminuser(models.Model):
    user_name = models.CharField(max_length=50)
    user_pass = models.CharField(max_length=264)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.user_name
