from django.core.management import BaseCommand
from movie.models import Genre


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        genre_list = (
            '드라마',
            '다큐멘터리',
            '코미디',
            '액션',
            '애니메이션',
            '공포',
            '스릴러',
            '로맨틱코미디',
            '범죄/느와르',
            '로맨스/멜로',
            'SF',
            '판타지',
            '전쟁',
            '가족/아동',
            '시트콤',
            '시대극',
            '음악',
            '스포츠',
            '틴에이저',
            '재난',
            '키즈',
            '예능',
            '단편',
            '시사교양',
        )
        for item in genre_list:
            Genre.objects.create(
                genre=item
            )
