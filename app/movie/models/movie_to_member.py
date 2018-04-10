from django.db import models

from actor_director.models import Member
from ..models import Movie

__all__ = (
    'MovieToMember',
)


class MovieToMember(models.Model):
    CHOICES_MEMBER_TYPE = (
        ('1', 'director'),
        ('2', 'scenario-writer'),
        ('3', 'etc-staff'),
        ('4', 'main-actor'),
        ('5', 'supporting-actor'),
        ('6', 'extra'),
    )

    movie = models.ForeignKey(
        Movie,
        related_name='movie_member_list',
        on_delete=models.CASCADE)
    member = models.ForeignKey(
        Member,
        related_name='casting_movie_list',
        on_delete=models.CASCADE)
    type = models.CharField('구성원 분류', max_length=5, choices=CHOICES_MEMBER_TYPE)
    role_name = models.CharField('배역', max_length=50, null=True, blank=True)
    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

    def __str__(self):
        return f'movie: {self.movie}, member: {self.member}'
