from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    body = models.TextField()


class Author(models.Model):
    name = models.CharField(max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author)
