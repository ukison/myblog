from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    body = models.TextField()
