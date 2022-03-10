from statistics import mode
from django.db import models

class studInfo(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.BigIntegerField()