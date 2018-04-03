from django.db import models
from django.contrib.auth.models import AbstractUser

from movie.models import Movie


class User(AbstractUser):
    img_profile = models.ImageField('프로필 사진', upload_to='user', blank=True)
    nickname = models.CharField('별명', max_length=100, blank=True)

    movies = models.ManyToManyField(Movie, verbose_name='영화 목록', blank=True)
    pass
