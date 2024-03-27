from django.db import models

# Create your models here.

class Enquiry(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(null=True)
    Mobile = models.CharField(max_length=25,null=True)
    Subject = models.CharField(max_length=50,null=True)
    Description = models.TextField()

    def __str__(self):
        return self.Name
    
class Review(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return self.Name