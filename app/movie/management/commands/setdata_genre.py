from django.core.management import BaseCommand
from movie.models import Genre


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        genre_list = (
            '액션',
            '로맨틱코미디',
            '미스터리',
            '범죄',
            '스릴러',
            '드라마',
            '가족',
            '애니메이션',
            '멜로/로맨스',
            '판타지',
            '코미디',
            '다큐멘터리',
            '모험',
            '서스펜스',
            '공포',
            '블랙코미디',
            'SF',
            '전쟁',
            '뮤지컬',
            '느와르',
            '서사',
            '무협',
        )
        for item in genre_list:
            obj, created = Genre.objects.get_or_create(
                genre=item
            )
        self.stdout.write(self.style.SUCCESS('Success: setdata_genre command'))
