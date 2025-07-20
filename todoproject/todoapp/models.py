from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.EmailField()
    phone=models.CharField(max_length=20)

class Tasks(models.Model):
    name=models.CharField(max_length=20)
    date=models.DateField(null=False)