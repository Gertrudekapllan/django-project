from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    country = models.CharField(max_length=100)


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    page_count = models.IntegerField()
    isbn = models.CharField(max_length=20)
    genres = models.ManyToManyField(Genre)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
