from django.db import models
from django.contrib.auth.models import User as AU


# Create your models here.
class User(models.Model):
    user = models.OneToOneField(AU, default=0, on_delete=models.CASCADE)
    loyalty_points = models.IntegerField(default=0)
    profile_picture = models.ImageField(null=True, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')


