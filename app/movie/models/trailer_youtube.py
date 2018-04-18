from django.db import models

from ..models import Movie

__all__ = (
    'TrailerYouTube',
)


class TrailerYouTube(models.Model):
    # Youtube 예고편을 추가하기 위한 모델 OneToMany
    movie = models.ForeignKey(Movie, related_name='trailer_youtube', verbose_name='영화', on_delete=models.CASCADE, blank=True, null=True)
    youtube_id = models.CharField('YouTube ID', max_length=20)
    title = models.CharField('제목', max_length=200, null=True, blank=True)
    url_thumbnail = models.URLField(
        '커버 이미지 URL',
        max_length=200,
        blank=True,
        help_text='this image is 320px wide and 180px tall.'
    )
    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'({self.id}) {self.title}'

    @property
    def get_trailer_url(self):
        return f'https://youtu.be/{self.youtube_id}'

