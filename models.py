from django.db import models

# Create your models here.
class CustomerTable(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Gender = models.CharField(max_length=10,null=True)
    Email_Id = models.CharField(max_length=50,null=True)
    Password = models.CharField(max_length=50,null=True)