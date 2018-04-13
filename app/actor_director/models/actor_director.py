from django.db import models

__all__ = (
    'Member',
)


class Member(models.Model):
    actor_director_id = models.CharField('감독/배우 아이디', max_length=10, unique=True, null=True, blank=True)
    name = models.CharField('이름', max_length=50)
    real_name = models.CharField('본명', max_length=50, null=True, blank=True)
    img_profile = models.ImageField(upload_to='members', blank=True)
    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

    def __str__(self):
        return self.name

    # def __str__(self):
    #     return f'이름: {self.name}, type: {self.casting_movie_list.objects.type}'


