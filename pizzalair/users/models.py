from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.template.defaultfilters import slugify
import os


# Create your models here.
class User(AbstractUser):
    loyalty_points = models.IntegerField(default=0)
    profile_picture = models.ImageField(null=True, default='blank-profile-picture.webp', upload_to='profile_pics')


    # resizing images
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.profile_picture.path)



        if img.height > 200 or img.width > 200:
            new_img = (200, 200)
            img.thumbnail(new_img)
            img.save(self.profile_picture.path)
