from rest_framework import serializers
from movie.serializers.movie_to_member_serializer import MovieToMemberListSerializer
from ..serializers import GenreSerializer
from ..models import Movie

__all__ = (
    'MovieListSerializer',
    'MovieMinimumListSerializer',
    'WantWatchedMovieListSerializer',
    'MovieBoxOfficeRankingSerializer',
)


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieMinimumListSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'poster_image',
            'rating_avg',
            'genre',
            'tag',
        )


class MovieBoxOfficeRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'ticketing_rate',
            'poster_image',
            'rating_avg',
        )
        # ordering = ('tiketing_rate',)


class WantWatchedMovieListSerializer(MovieListSerializer):
    genre = GenreSerializer(many=True)

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
        )


class MovieDetailListSerializer(serializers.ModelSerializer):
    members = MovieToMemberListSerializer(source='movie_member_list', many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

# class MovieListSerializer(serializers.ModelSerializer):
#     movietomember_set = MovieToMemberListSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Movie
#         fields = (
#             'id',
#             'title_ko',
#             'ticketing_rate',
#             'poster_image',
#             'rating_avg',
#             'movie_created_date',
#             'd_day',
#             'film_rate',
#             'running_time',
#             'intro',
#             'nation',
#             'ticketing_rate',
#             'audience',
#             'poster_image',
#             'rating_avg',
#             'members',
#             'genre',
#             'tag',
#             'modified_date',
#             'created_date',
#             'user',
#         )
