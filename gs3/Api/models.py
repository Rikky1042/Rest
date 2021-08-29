from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    Class=models.CharField(max_length=100)
    School=models.CharField(max_length=100)
    mobile=models.IntegerField()