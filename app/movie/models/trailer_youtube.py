from django.db import models
from movie.models import Movie


__all__ = (
    'TrailerYouTube',
)


class TrailerYouTube(models.Model):
    # Youtube 예고편을 추가하기 위한 모델 OneToMany
    movie = models.ForeignKey(Movie, verbose_name='영화', on_delete=models.CASCADE, blank=True, null=True)
    youtube_id = models.CharField('YouTube ID', primary_key=True, max_length=20)
    title = models.CharField('제목', max_length=200)
    url_thumbnail = models.URLField('커버 이미지 URL', max_length=200, blank=True)
    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

