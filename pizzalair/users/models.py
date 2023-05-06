from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    #user = models.OneToOneField(on_delete=models.CASCADE, null=True)
    loyalty_points = models.IntegerField(default=0)
    profile_picture = models.ImageField(null=True, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')


