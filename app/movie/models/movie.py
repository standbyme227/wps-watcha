import magic
from PIL import Image
from django.core.files import File
from django.core.validators import MaxValueValidator
from django.db import models
from io import BytesIO

from actor_director.models import Member
from django.conf import settings
from .managers import MovieManager
from .genre import Genre
from .tag import Tag

__all__ = (
    'Movie',
)


class Movie(models.Model):
    LIMIT = 'limit'
    ETC = 'ETC'
    CHOICES_FILE_RATE_TYPE = (
        ('all', '전체 관람가'),
        ('12', '12세 관람가'),
        ('15', '15세 관람가'),
        ('18', '18세 관람가'),
        ('limit', '청소년 관람불가'),
        (ETC, '기타'),
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
    title_en = models.CharField('영화제목(영문)', max_length=100, blank=True)  # (구)title_detail
    title_slug = models.SlugField(null=True, blank=True)

    movie_created_date = models.IntegerField('제작년도', null=True, blank=True)

    d_day = models.DateField('개봉일', max_length=50, null=True, blank=True)
    film_rate = models.CharField('상영 등급', max_length=10, choices=CHOICES_FILE_RATE_TYPE, blank=True)
    running_time = models.IntegerField('상영시간', null=True, blank=True)
    intro = models.TextField('줄거리', blank=True)  # (구)story
    nation = models.CharField('국가', max_length=5, choices=CHOICES_NATION_CODE, blank=True)
    ticketing_rate = models.DecimalField('예매율', default=0.0, max_digits=5, decimal_places=2,
                                         validators=[MaxValueValidator(100), ], blank=True, null=True)  # (구)rank_share
    audience = models.IntegerField('누적관객수', null=True, blank=True)
    poster_image = models.ImageField('포스터 이미지', upload_to='poster', blank=True)
    poster_image_m = models.ImageField('중간 포스터 이미지', upload_to='poster', blank=True)
    poster_image_s = models.ImageField('작은 포스터 이미지', upload_to='poster', blank=True)
    poster_image_my_x3 = models.ImageField('IOS mypage x3', upload_to='poster/ios/my', blank=True)
    poster_image_box_x3 = models.ImageField('IOS box office x3', upload_to='poster/ios/box', blank=True)
    poster_image_eval_x3 = models.ImageField('IOS eval x3', upload_to='poster/ios/eval', blank=True)

    rating_avg = models.DecimalField('평점평균', default=0.0, max_digits=2, decimal_places=1,
                                     validators=[MaxValueValidator(5), ], blank=True, )
    members = models.ManyToManyField(
        Member,
        through='MovieToMember',
        blank=True,
    )

    genre = models.ManyToManyField(
        Genre,
        through='MovieToGenre',
        blank=True
    )

    tag = models.ManyToManyField(
        Tag,
        blank=True
    )

    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='UserToMovie',
        blank=True,
    )

    class Meta:
        ordering = ['-pk']

    objects = MovieManager()

    def __str__(self):
        return self.title_ko

    def give_rating_user(self, user, rating):
        rating, rating_created = self.interested_user_list.get_or_create(
            user=user,
            rating=rating,
        )
        if not rating_created:
            rating.delete()
        return rating_created

    def save(self, *args, **kwargs):
        self._save_resizing_process()
        super().save(*args, **kwargs)

    def _save_resizing_process(self):

        if self.poster_image:
            # 이미지파일의 이름과 확장자를 가져옴
            full_name = self.poster_image.name.rsplit('/')[-1]
            full_name_split = full_name.rsplit('.', maxsplit=1)

            temp_file = BytesIO()
            temp_file.write(self.poster_image.read())
            temp_file.seek(0)
            mime_info = magic.from_buffer(temp_file.read(), mime=True)
            temp_file.seek(0)

            name = full_name_split[0]
            ext = mime_info.split('/')[-1]

            # Pillow를 사용해 이미지 파일 로드
            im = Image.open(self.poster_image)

            medium = im.resize((220, 314))
            temp_file = BytesIO()
            medium.save(temp_file, ext)
            self.poster_image_m.save(f'{name}_medium.{ext}', File(temp_file), save=False)

            small = im.resize((140, 200))
            temp_file = BytesIO()
            small.save(temp_file, ext)
            self.poster_image_s.save(f'{name}_small.{ext}', File(temp_file), save=False)

            my_x3 = im.resize((225, 342))
            temp_file = BytesIO()
            my_x3.save(temp_file, format="JPEG", quality=70, optimize=True, progressive=True)
            self.poster_image_my_x3.save(f'{name}_my_x3.{ext}', File(temp_file), save=False)

            # my_x2 = im.resize((150, 228))
            # temp_file = BytesIO()
            # my_x2.save(temp_file, ext, optimize=True, progressive=True)
            # self.poster_image_my_x2.save(f'{name}_my_x2.{ext}', File(temp_file), save=False)
            #
            # my_x1 = im.resize((75, 114))
            # temp_file = BytesIO()
            # my_x1.save(temp_file, ext, optimize=True, progressive=True)
            # self.poster_image_my_x1.save(f'{name}_my_x1.{ext}', File(temp_file), save=False)

            box_x3 = im.resize((291, 408))
            temp_file = BytesIO()
            box_x3.save(temp_file, format="JPEG", quality=70, optimize=True, progressive=True)
            self.poster_image_box_x3.save(f'{name}_box_x3.{ext}', File(temp_file), save=False)

            # box_x2 = im.resize((194, 272))
            # temp_file = BytesIO()
            # box_x2.save(temp_file, format="JPEG", quality=70, optimize=True, progressive=True)
            # self.poster_image_box_x2.save(f'{name}_box_x2.{ext}', File(temp_file), save=False)
            #
            # box_x1 = im.resize((97, 136))
            # temp_file = BytesIO()
            # box_x1.save(temp_file, format="JPEG", quality=70, optimize=True, progressive=True)
            # self.poster_image_box_x1.save(f'{name}_box_x1.{ext}', File(temp_file), save=False)

            eval_x3 = im.resize((189, 270))
            temp_file = BytesIO()
            eval_x3.save(temp_file, format="JPEG", quality=70, optimize=True, progressive=True)
            self.poster_image_eval_x3.save(f'{name}_eval_x3.{ext}', File(temp_file), save=False)

            # eval_x2 = im.resize((126, 180))
            # temp_file = BytesIO()
            # eval_x2.save(temp_file, format="JPEG", quality=70, optimize=True, progressive=True)
            # self.poster_image_eval_x2.save(f'{name}_eval_x2.{ext}', File(temp_file), save=False)
            #
            # eval_x1 = im.resize((63, 90))
            # temp_file = BytesIO()
            # eval_x1.save(temp_file, format="JPEG", quality=70, optimize=True, progressive=True)
            # self.poster_image_eval_x1.save(f'{name}_eval_x1.{ext}', File(temp_file), save=False)

        else:
            self.poster_image_m.delete(save=False) \
            and self.poster_image_s.delete(save=False) \
            and self.poster_image_my_x3.delete(save=False) \
            and self.poster_image_box_x3.delete(save=False) \
            and self.poster_image_eval_x3.delete(save=False)

            # else:
        #     self.poster_image_my_x3.delete(save=False) \
        #     and self.poster_image_my_x2.delete(save=False) \
        #     and self.poster_image_my_x1.delete(save=False) \
        #     and self.poster_image_box_x3.delete(save=False) \
        #     and self.poster_image_box_x2.delete(save=False) \
        #     and self.poster_image_box_x1.delete(save=False) \
        #     and self.poster_image_eval_x3.delete(save=False) \
        #     and self.poster_image_eval_x2.delete(save=False) \
        #     and self.poster_image_eval_x1.delete(save=False)
