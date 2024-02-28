from django.db import models
from U_Auth.models import User

# Create your models here.

class Place(models.Model):
    Status = models.IntegerField(default=1)
    Name = models.CharField(max_length=100)
    Added_Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Name
    

class Agents(models.Model):
    Status = models.IntegerField(default=1)
    Name = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=25)
    Email = models.EmailField(null=True)
    Place = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
    
class Course(models.Model):
    Status = models.IntegerField(default=1)
    Added_Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
    
class Collage(models.Model):
    Status = models.IntegerField(default=1)
    Name = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=25)
    Email = models.EmailField(null=True)
    Place = models.ForeignKey(Place,on_delete=models.DO_NOTHING)
    Agent = models.ForeignKey(Agents,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Name
    

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=15)
    Email = models.EmailField()
    Place = models.CharField(max_length=50)

    Collage = models.ForeignKey(Collage,on_delete=models.DO_NOTHING)
    Course = models.ForeignKey(Course,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Name