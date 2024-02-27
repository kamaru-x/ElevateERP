from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_developer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_telecaller = models.BooleanField(default=False)

    Image = models.ImageField(upload_to='Staffs',null=True)
    Mobile = models.CharField(max_length=25,null=True)
    Place = models.CharField(max_length=35,null=True)
    

    def __str__(self):
        return self.username