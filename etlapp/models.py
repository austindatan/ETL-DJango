from django.db import models

# Create your models here.

class RawIMDB(models.Model):
    imdb_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    release_year = models.IntegerField(null=True)
    genre = models.CharField(max_length=100)
    duration = models.IntegerField(null=True)
    country = models.CharField(max_length=100)
    content_rating = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    income = models.BigIntegerField(null=True)

    def __str__(self):
        return self.title

class CleanIMDB(models.Model):
    imdb_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    release_year = models.IntegerField(null=True)
    genre = models.CharField(max_length=100)
    duration = models.IntegerField(null=True)
    country = models.CharField(max_length=100)
    content_rating = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    income = models.BigIntegerField(null=True)

    def __str__(self):
        return self.title