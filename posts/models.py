from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Post(models.Model):
    book_title = models.CharField(max_length=128)
    book_author = models.CharField(max_length=128)
    body = models.TextField()
    post_author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        Status,
        on_delete = models.CASCADE,
        null=True, default=None
    )

    def __str__(self):
        return self.book_title

    def get_absolute_url(self):
        return reverse("details", args=[self.id])



# class UserProfile(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='profile'
#     )
#     bio = models.TextField(blank=True)
#     profile_image = models.ImageField(upload_to='profile_images', blank=True)
#     username = models.TextField()
#     password = models.TextField()

# class CustomUser(AbstractUser):
#     User = get_user_model()
#     bio = models.TextField(blank=True)
#     profile_image = models.ImageField(upload_to='profile_images', blank=True)
