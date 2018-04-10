from django.core.validators import MaxValueValidator
from django.db import models

from .managers import MovieManager

__all__ = (
    'Movie',
)


class Movie(models.Model):
    KOREA = 'KR'
    JAPAN = 'JP'
    CHINA = 'CH'
    UNITEDSTATE = 'US'
    HONGKONG = 'HK'
    GREAT_BRITAIN = 'GB'
    FRANCE = 'FR'
    GERMAN = 'GM'
    ITALY = 'IT'
    THAILAND = 'TH'
    ETC = 'ETC'
    CHOICES_NATION_CODE = (
        (KOREA, '한국'),
        (JAPAN, '일본'),
        (CHINA, '중국'),
        (UNITEDSTATE, '미국'),
        (HONGKONG, '홍콩'),
        (GREAT_BRITAIN, '영국'),
        (FRANCE, '프랑스'),
        (GERMAN, '독일'),
        (ITALY, '이탈리아'),
        (THAILAND, '태국'),
        (ETC, 'None'),
    )

    naver_movie_id = models.CharField('Naver의 Movie ID', max_length=20, blank=True, null=True, unique=True)

    title_ko = models.CharField('영화제목', max_length=100)
    title_detail = models.CharField(max_length=100, blank=True, null=True)

    nation = models.CharField('국가', max_length=100, blank=True, choices=CHOICES_NATION_CODE)

    running_time = models.CharField('상영시간', max_length=100, blank=True )
    film_rate = models.CharField('상영 등급', max_length=100, blank=True)

    rank_share = models.CharField('예매율', max_length=100, blank=True)
    audience = models.IntegerField('누적관객수', blank=True, null=True)

    story = models.TextField('줄거리', blank=True)
    poster_image = models.ImageField('포스터 이미지', upload_to='poster', blank=True)
    still_cut = models.ImageField('스틸컷', upload_to='still_image', blank=True)
    # img확인


    d_day = models.DateField('개봉일',max_length=50, blank=True, null=True)

    rating_avg = models.DecimalField('별점', max_digits=2,
                                     decimal_places=1, validators=[MaxValueValidator(5),], blank=True, null=True)

    # genre = models.ManytoManyField('장르', max_length=100, blank=True)
    # tag = models.ManyToManyField


    # trailer = MVP 모델은 아니다

    # derector =
    # actors =

    class Meta:
        ordering = ['-pk']

    objects = MovieManager()