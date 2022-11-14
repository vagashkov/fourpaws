from django.db import models


class Post(models.Model):
    caption = models.TextField()
    text = models.TextField()

