from django.db import models

__all__ = (
    'Genre',
)


class Genre(models.Model):
    DRAMA = 1
    FANTASY = 2
    WESTERN = 3
    HORROR = 4
    ROMANCE = 5
    ADVENTURE = 6
    THRILLER = 7
    NOIR = 8
    CULT = 9
    DOCUMENTARY = 10
    COMEDY = 11
    FAMILY = 12
    MISTERY = 13
    WAR = 14
    ANIMATION = 15
    CRIMINAL = 16
    MUSICAL = 17
    SF = 18
    ACTION = 19
    MATIAL_ARTS = 20
    ADULT = 21
    SUSPENSE = 22
    NARRATIVE = 23
    BLACKCOMEDY = 24
    EXPERIMENT = 25
    MOVIECARTOON = 26
    MOVIEMUSIC = 27
    PARODY = 28
    ETC = 29

    CHOICES_GENRE_TYPE = (
        (DRAMA, '드라마'),
        (FANTASY, '판타지'),
        (WESTERN, '서부'),
        (HORROR, '공포'),
        (ROMANCE, '로맨스'),
        (ADVENTURE, '모험'),
        (THRILLER, '스릴러'),
        (NOIR, '느와르'),
        (CULT, '컬트'),
        (DOCUMENTARY, '다큐멘터리'),
        (COMEDY, '코미디'),
        (FAMILY, '가족'),
        (MISTERY, '미스터리'),
        (WAR, '전쟁'),
        (ANIMATION, '애니메이션'),
        (CRIMINAL, '범죄'),
        (MUSICAL, '뮤지컬'),
        (SF, 'SF'),
        (ACTION, '액션'),
        (MATIAL_ARTS, '무협'),
        (ADULT, '에로'),
        (SUSPENSE, '서스펜스'),
        (NARRATIVE, '서사'),
        (BLACKCOMEDY, '블랙코미디'),
        (EXPERIMENT, '실험'),
        (MOVIECARTOON, '영화카툰'),
        (MOVIEMUSIC, '영화음악'),
        (PARODY, '영화패러디포스터'),
        (ETC, '기타')
    )

    genre = models.CharField('장르', max_length=20, choices=CHOICES_GENRE_TYPE, unique=True)
    modified_date = models.DateTimeField('수정일시', auto_now=True)
    created_date = models.DateTimeField('생성일시', auto_now_add=True)

    def __str__(self):
        return self.genre

