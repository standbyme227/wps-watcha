from django.db import models

__all__ = (
    'Genre',
)


class Genre(models.Model):
    genre = models.CharField('장르', max_length=20, unique=True)
    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

    def __str__(self):
        return self.genre

