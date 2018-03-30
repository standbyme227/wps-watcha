from django.db import models
from django.contrib.auth.models import AbstractUser
from movie.models import Movie


class User(AbstractUser):
    movies = models.ManyToManyField(Movie, verbose_name='영화 목록', blank=True)
    pass
