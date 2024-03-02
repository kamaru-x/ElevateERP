from django.db import models
from U_Auth.models import User

# Create your models here.

RANK = [
    ('Main','Main'),
    ('Sub','Sub')
]

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
    # Place = models.CharField(max_length=50)
    Rank = models.CharField(choices=RANK,max_length=50)

    def __str__(self):
        return self.Name
    
class Course(models.Model):
    Status = models.IntegerField(default=1)
    Added_Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
    
class Course_Addon(models.Model):
    Course = models.ForeignKey(Course,on_delete=models.CASCADE)
    Title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Course}-{self.Title}'
    
class Collage(models.Model):
    Status = models.IntegerField(default=1)
    Name = models.CharField(max_length=100)
    Place = models.ForeignKey(Place,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Name
    

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=15)
    Email = models.EmailField(null=True)
    Place = models.CharField(max_length=50,null=True)

    Collage = models.ForeignKey(Collage,on_delete=models.DO_NOTHING)
    Course = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    Addon = models.ForeignKey(Course_Addon,on_delete=models.DO_NOTHING,null=True)
    Sub_Agent = models.ForeignKey(Agents,on_delete=models.DO_NOTHING,null=True,related_name='sub_agent')
    Main_Agent = models.ForeignKey(Agents,on_delete=models.DO_NOTHING,null=True,related_name='main_agent') 

    Fees = models.FloatField(default=0.00)
    Donation = models.FloatField(default=0.00)
    Discount = models.FloatField(default=0.00)
    Total = models.FloatField(default=0.00)
    First_Payment = models.FloatField(default=0.00)
    Service = models.FloatField(default=0.00)
    Collage_Payment = models.FloatField(default=0.00)
    Agent_Commission = models.FloatField(default=0.00)

    def __str__(self):
        return self.Name