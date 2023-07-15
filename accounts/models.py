from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images', blank=True)
