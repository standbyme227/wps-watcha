from django.db import models
from movie.models import Movie


class Director(models.Model):
    movies = models.ManyToManyField(Movie, verbose_name='영화 목록', blank=True)
