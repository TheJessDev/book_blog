from django.db import models
from django.contrib.auth import get_user_model
from django.urls import path, reverse


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
        return self.title

    def get_absolute_url(self):
        return reverse("posts_details", args=[self.id])
