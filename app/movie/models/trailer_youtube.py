from django.db import models

from .movie import Movie

__all__ = (
    'TrailerYouTube',
)


class TrailerYouTube(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    youtube_id = models.CharField('YouTube ID', primary_key=True, max_length=20)
    title = models.CharField('제목', max_length=200)
    url_thumbnail = models.URLField(
        '커버 이미지 URL',
        max_length=200,
        blank=True,
        help_text='this image is 320px wide and 180px tall.'
    )
    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

    def __str__(self):
        return f'{self.youtube_id}: {self.title}'

    @property
    def get_trailer_url(self):
        return f'https://youtu.be/{self.youtube_id}'
