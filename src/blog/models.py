from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200, default="No title")
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, default=1)
    text = models.TextField()

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse('post_details', args=[str(self.id)])
