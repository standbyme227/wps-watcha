from rest_framework import serializers
from ...serializers import GenreSerializer
from ...models import Movie

__all__ = (
    'MovieListSerializer',
    'MovieMinimumListSerializer',
    'MovieNameBoxOfficeRankingSerializer',
)


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieMinimumListSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    tag = serializers.CharField(source='get_tag_display', read_only=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'movie_created_date',
            'poster_image_m',
            'rating_avg',
            'genre',
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

