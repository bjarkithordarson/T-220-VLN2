from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField(default=0)
    email = models.TextField(default=0)
    password = models.CharField(max_length=120)
    loyalty_points = models.IntegerField(default=0)
    #profile_picture = models.ImageField(default=Null)