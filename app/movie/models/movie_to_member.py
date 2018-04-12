from django.db import models

from actor_director.models import Member
from ..models import Movie

__all__ = (
    'MovieToMember',
)


class MovieToMember(models.Model):
    A = 1
    B = 2
    C = 3
    D = 4
    CHOICES_MEMBER_TYPE = (
        (A, '감독'),
        (B, '주연'),
        (C, '조연'),
        (D, '단역'),
    )

    movie = models.ForeignKey(Movie, related_name='movie_member_list', on_delete=models.CASCADE)
    member = models.ForeignKey(Member, related_name='casting_movie_list', on_delete=models.CASCADE)
    type = models.CharField('구성원 분류', max_length=5, choices=CHOICES_MEMBER_TYPE)
    role_name = models.CharField('배역', max_length=50, null=True, blank=True)
    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

    def __str__(self):
        return f'movie: {self.movie}, member: {self.member}'
