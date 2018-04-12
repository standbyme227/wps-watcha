from django.contrib.auth import get_user_model
from rest_framework import serializers

from movie.serializers import MovieSerializer, GenreSerializer
from movie.models import UserToMovie, Movie

User = get_user_model()

__all__ = (
    'UserToMovieSerializer',
)


class UserRelatedMovieSerializer(MovieSerializer):
    genre = GenreSerializer(many=True)

    # 장르의 텍스트만 리스트형태로 전달하고 싶을 때에는 아래처럼 SlugRelatedField를 사용
    # genre = serializers.SlugRelatedField(many=True, read_only=True, slug_field='genre')

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'title_en',
            'nation',
            'poster_image',
            'genre',
            'running_time',
        )


class UserToMovieSerializer(serializers.ModelSerializer):
    movie = UserRelatedMovieSerializer()

    class Meta:
        model = UserToMovie
        fields = '__all__'
