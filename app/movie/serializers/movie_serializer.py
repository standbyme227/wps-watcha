from rest_framework import serializers

from actor_director.serializers import MemberDetailSerializer
from ..models import Movie, UserToMovie
from ..serializers.genre_serializer import GenreSerializer
from ..serializers.stillcut_serializer import StillCutSerializer
from ..serializers.tag_serializer import TagSerializer
from ..serializers.user_to_movie_serializer import UserToMovieWantWatchedListSerializer

__all__ = (
    'MovieListSerializer',
    'MovieDetailSerializer',
    'MovieSimpleDetailSerializer',
    'WantWatchedMovieListSerializer',
)


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    # still_cuts = serializers.StringRelatedField(many=True)
    still_cuts = StillCutSerializer(many=True)
    genre = GenreSerializer(many=True)
    tag = TagSerializer(many=True)
    members = MemberDetailSerializer(many=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'title_en',
            'd_day',
            'film_rate',
            'running_time',
            'intro',
            'nation',
            'ticketing_rate',
            'audience',
            'rating_avg',
            'poster_image',
            'still_cuts',
            'genre',
            'tag',
            'members',
            'user',
        )


class MovieSimpleDetailSerializer(serializers.ModelSerializer):
    login_user_checked = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'poster_image',
            'login_user_checked',
        )

    def get_login_user_checked(self, obj):
        items = UserToMovie.objects.filter(user=self.context['login_user'], movie=obj)
        if len(items) == 1:
            for item in items:
                serializer = UserToMovieWantWatchedListSerializer(item)
                return serializer.data
        elif len(items) == 0:
            return {'no-data': 'does not exist.'}
        else:
            return {'error': 'Problems with data consistency'}


class WantWatchedMovieListSerializer(MovieListSerializer):
    genre = GenreSerializer(many=True)
    # movie_id = serializers.IntegerField(source='id')
    login_user_checked = serializers.SerializerMethodField()
    # 장르의 텍스트만 리스트형태로 전달하고 싶을 때에는 아래처럼 SlugRelatedField를 사용
    # genre = serializers.SlugRelatedField(many=True, read_only=True, slug_field='genre')

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'title_en',
            'rating_avg',
            'nation',
            'poster_image',
            'genre',
            'running_time',
            'login_user_checked',
        )

    def get_login_user_checked(self, obj):
        items = UserToMovie.objects.filter(user=self.context['login_user'], movie=obj)
        if len(items) == 1:
            for item in items:
                serializer = UserToMovieWantWatchedListSerializer(item)
                return serializer.data
        elif len(items) == 0:
            return {'no-data': 'does not exist.'}
        else:
            return {'error': 'Problems with data consistency'}
