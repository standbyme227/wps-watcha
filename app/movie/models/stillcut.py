from django.db import models

from ..models import Movie

__all__ = (
    'StillCut',
)


class StillCut(models.Model):
    # stillcut 추가할 모델 OneToMany
    movie = models.ForeignKey(Movie, verbose_name='영화', on_delete=models.CASCADE, blank=True, null=True)
    still_img = models.ImageField('스틸 이미지', upload_to='still_cut', blank=True)
    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.id} - {self.movie.title_ko}'
