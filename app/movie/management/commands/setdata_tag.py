from django.core.management import BaseCommand

from movie.models import Tag


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        tag_list = (
            '소설원작',
            '스릴있는',
            '서부극',
            '사극',
            '어드벤쳐',
            '정글',
            '바다',
        )
        for item in tag_list:
            Tag.objects.create(
                tag=item
            )
