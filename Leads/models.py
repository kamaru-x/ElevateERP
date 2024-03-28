from django.db import models
from U_Auth.models import User

# Create your models here.

class Leads(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=25,default='PENDING')
    Name = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=25)
    Place = models.CharField(max_length=50)

    Staff = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)

    def __str__(self):
        return self.Name
    
class Lead_Timeline(models.Model):
    Lead = models.ForeignKey(Leads,on_delete=models.CASCADE)
    Date = models.DateTimeField()
    Title = models.TextField()
    Color = models.CharField(max_length=15,null=True)