from django.contrib.auth import admin
from django.db import models


class Category(models.Model):
    GENRE_CHOICES = [
        ('horror', 'Horror Movies: '),
        ('action', 'Action Movies: '),
        ('comedy', 'Comedy Movies: '),
        ('drama', 'Drama Movies: '),
        ('fantasy', 'Fantasy Movies: '),
        ('mystery', 'Mystery Movies: '),
        ('romance', 'Romance '),
        ('thriller', 'Thriller'),
    ]

    name = models.CharField(max_length=100, choices=GENRE_CHOICES)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    actor = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    year = models.IntegerField()
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
        return self.name




