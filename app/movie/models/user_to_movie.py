from django.db import models

from config import settings
from ..models import Movie

__all__ = (
    'UserToMovie',
)


class UserToMovie(models.Model):
    # User랑 Movie를 위한 중개모델

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='interesting_movie_list',
        on_delete=models.CASCADE,
    )

    movie = models.ForeignKey(
        Movie,
        related_name='interested_user_list',
        on_delete=models.CASCADE,
    )
    user_want_movie = models.BooleanField('보고싶은 영화', default=False)
    user_watched_movie = models.BooleanField('본 영화', default=False)
    rating = models.DecimalField('평점', max_digits=2, decimal_places=1, null=True, blank=True)
    comment = models.TextField('코멘트', blank=True)
    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

    class Meta:
        unique_together = (
            ('user', 'movie'),
        )

    def __str__(self):
        return f'UserToMovie (User: {self.user}, Movie: {self.movie})'
