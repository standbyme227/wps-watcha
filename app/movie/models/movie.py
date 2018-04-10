from django.core.validators import MaxValueValidator
from django.db import models

from config import settings
from actor_director.models import Member
from .managers import MovieManager
from .genre import Genre
from .stillcut import StillCut
from .tag import Tag
from .trailer_youtube import TrailerYouTube

__all__ = (
    'Movie',
)


class Movie(models.Model):
    CHOICES_FILE_RATE_TYPE = (
        ('all', '전체 관람가'),
        ('12', '12세 관람가'),
        ('15', '15세 관람가'),
        ('18', '18세 관람가'),
        ('limit', '제한상영가'),
    )

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
        (ETC, '기타'),
    )

    naver_movie_id = models.CharField('네이버 영화 아이디', max_length=10, unique=True, null=True, blank=True)
    title_ko = models.CharField('영화제목(한글)', max_length=100, blank=True)
    title_en = models.CharField('영화제목(영문)', max_length=100, blank=True) # (구)title_detail
    title_slug = models.SlugField(null=True, blank=True)
    genre = models.ManyToManyField(
        Genre,
        blank=True
    )
    tag = models.ManyToManyField(
        Tag,
        blank=True
    )
    rating_avg = models.DecimalField('평점평균', default=0.0, max_digits=2, decimal_places=1, validators=[MaxValueValidator(5), ])
    d_day = models.DateField('개봉일', max_length=50, null=True, blank=True)
    film_rate = models.CharField('상영 등급', max_length=10, choices=CHOICES_FILE_RATE_TYPE, blank=True)
    running_time = models.IntegerField('상영시간', null=True, blank=True)
    intro = models.TextField('줄거리', blank=True) # (구)story
    nation = models.CharField('국가', max_length=5, choices=CHOICES_NATION_CODE, blank=True)
    ticketing_rate = models.CharField('예매율', max_length=10, blank=True) # (구)rank_share
    audience = models.IntegerField('누적관객수', null=True, blank=True)

    Poster_image = models.ImageField('포스터 이미지', upload_to='poster', blank=True)
    still_cut = models.ManyToManyField(
        StillCut,
        blank=True
    )
    members = models.ManyToManyField(
        Member,
        through='MovieToMember',
        blank=True
    )
    trailer = models.ManyToManyField(
        TrailerYouTube,
        blank=True
    )
    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='UserToMovie',
        blank=True,
    )
    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

    class Meta:
        ordering = ['-pk']

    objects = MovieManager()

    def __str__(self):
        return self.title_ko
