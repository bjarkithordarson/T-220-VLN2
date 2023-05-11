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



        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.profile_picture.path)

class LoyaltyPoints(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.points} points"

class LoyaltyPointsTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.points} points - {self.date}"
