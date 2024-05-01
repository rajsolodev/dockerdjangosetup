from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.CharField(max_length=255)
