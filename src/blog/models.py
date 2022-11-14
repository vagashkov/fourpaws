from django.db import models


class Post(models.Model):
    caption = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.caption[:50]
