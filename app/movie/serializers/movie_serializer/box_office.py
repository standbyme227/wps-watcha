from rest_framework import serializers
from movie.serializers.user_to_movie_serializer import UserToMovieCommentListSerializer
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
            'poster_image_m',
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
    film_rate = serializers.CharField(source='get_film_rate_display', read_only=True)
    user = UserToMovieCommentListSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'movie_created_date',
            'ticketing_rate',
            'rating_avg',
            'poster_image',
            'poster_image_m',
            'd_day',
            'audience',
            'film_rate',
            'running_time',
            'genre',
            'user'
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
            'poster_image_m',
            'members',
            'd_day',
            'audience',
            'film_rate',
            'running_time',
        )
