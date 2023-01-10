from django.db import models

class Login(models.Model):
    login_name=models.CharField(verbose_name='Username',max_length=50)
    login_password=models.CharField(verbose_name='Password',max_length=256)
    create_date=models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.login_name
    