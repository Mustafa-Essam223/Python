from django.db import models

# Create your models here.
class employee(models.Model):
    Name=models.CharField(max_length=30,null=True)
    idd=models.IntegerField()
    email=models.EmailField(null=True)
    salary=models.FloatField(null=True)
    creationTime = models.DateTimeField(auto_now_add=True, null=True)
    updateTime = models.DateTimeField(auto_now=True, null=True)



