from django.db import models
from Core.models import Collage,Agents,Student
from U_Auth.models import User

# Create your models here.

TYPE = (('Income','Income'),('Expense','Expense'))

class Entry_Categories(models.Model):
    Title = models.CharField(max_length=100)
    Type = models.CharField(max_length=50,choices=TYPE)
    FOT = models.CharField(max_length=10,default='Elevate')

    def __str__(self):
        return self.Title
    
class Entry(models.Model):
    Title = models.CharField(max_length=100)
    Category = models.ForeignKey(Entry_Categories,on_delete=models.DO_NOTHING)
    Date = models.DateTimeField()
    Amount = models.FloatField(default=0.00)

    Collage = models.ForeignKey(Collage,on_delete=models.SET_NULL,null=True)
    Agents = models.ForeignKey(Agents,on_delete=models.SET_NULL,null=True)
    Student = models.ForeignKey(Student,on_delete=models.SET_NULL,null=True)
    Staff = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.Title