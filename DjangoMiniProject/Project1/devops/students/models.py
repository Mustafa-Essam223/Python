from django.db import models
# to use database
# Create your models here.

class student(models.Model):
    first_name=models.CharField(max_length=30,null=True)
    last_name=models.CharField(max_length=20,null=True)
    grade=models.IntegerField(default=0,null=True)
    email=models.EmailField(null=True)
    creationTime=models.DateTimeField(auto_now_add=True,null=True)
    updateTime=models.DateTimeField(auto_now=True,null=True)

