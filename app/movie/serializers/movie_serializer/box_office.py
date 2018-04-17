from rest_framework import serializers, filters
from rest_framework.compat import MaxValueValidator
from movie.serializers.movie_to_member_serializer import MovieToMemberListSerializer
from ...serializers import GenreSerializer
from ...models import Movie

__all__ = (
    'MovieMinimumListSerializer',
    'MovieNameBoxOfficeRankingSerializer',
    'MovieBoxOfficeRankingFiveSerializer',
    'MovieBoxOfficeRankingSerializer',

)


class MovieMinimumListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'poster_image',
            'rating_avg',
            'tag',
        )


class MovieNameBoxOfficeRankingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'ticketing_rate',
            'rating_avg',
        )


class MovieBoxOfficeRankingFiveSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    film_rate = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'ticketing_rate',
            'rating_avg',
            'poster_image',
            'd_day',
            'audience',
            'film_rate',
            'running_time',
            'genre',
        )


class MovieBoxOfficeRankingSerializer(serializers.ModelSerializer):
    members = MovieToMemberListSerializer(source='movie_member_list', many=True, read_only=True)
    film_rate = serializers.CharField(source='get_type_display', read_only=True)
    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'ticketing_rate',
            'rating_avg',
            'poster_image',
            'members',
            'd_day',
            'audience',
            'film_rate',
            'running_time',
        )

