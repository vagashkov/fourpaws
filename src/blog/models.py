from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, default="No title")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    text = models.TextField()

    def __str__(self):
        return self.title[:50]
