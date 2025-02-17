from django.db import models

# Create your models here.


class User_tbl(models.Model):
    name=models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
