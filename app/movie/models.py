from django.core.validators import MaxValueValidator
from django.db import models


class Movie(models.Model):
    title = models.CharField('영화제목', max_length=100)
    rating = models.PositiveIntegerField('별점', validators=[MaxValueValidator(5), ])
    running_time = models.CharField('상영시간', max_length=100, blank=True )
    film_rate = models.CharField('상영 등급', max_length=100, blank=True)



    nation = models.CharField('국가', max_length=100, blank=True)
    genre = models.CharField('장르', max_length=100, blank=True)

    intro = models.TextField('소개', blank=True)
    rank_share = models.CharField('예매율', max_length=100, blank=True)
    audience = models.IntegerField('관객수', blank=True)

    Poster_image = models.ImageField('포스터 이미지', upload_to='poster', blank=True)
    still_cut =models.ImageField('스틸컷', upload_to='still_image', blank=True)
    d_day = models.DateField(max_length=50, blank=True, null=True)


    # derector =
    # actors =