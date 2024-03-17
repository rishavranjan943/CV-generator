from django.db import models
from users.models import *
# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    summary=models.TextField(max_length=500,null=True,blank=True)
    degree=models.CharField(max_length=100,null=True,blank=True)
    school=models.CharField(max_length=100,null=True,blank=True)
    college=models.CharField(max_length=100,null=True,blank=True)
    experience=models.TextField(max_length=500,null=True,blank=True)
    skills=models.TextField(max_length=500,null=True,blank=True)

    def __str__(self) -> str:
        return self.name