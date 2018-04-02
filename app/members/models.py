from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from movie.models import Movie


class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    movies = models.ManyToManyField(Movie, verbose_name='영화 목록', blank=True)
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    nickname = models.CharField(verbose_name='nickname', max_length=20, blank=False, unique=True, default='')
    img_profile = models.ImageField(upload_to='user', blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

