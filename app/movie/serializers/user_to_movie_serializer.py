from django.contrib.auth import get_user_model
from rest_framework import serializers

from movie.serializers.movie_serializer.my_page import WantWatchedMovieListSerializer
from ..models import UserToMovie

User = get_user_model()

__all__ = (
    'UserToMovieBasicSerializer',
    'UserToMovieIncludeMovieInfoSerializer',
    'UserToMovieUpdateSerializer',
)


class UserToMovieBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToMovie
        fields = '__all__'


class UserToMovieIncludeMovieInfoSerializer(serializers.ModelSerializer):
    movie = WantWatchedMovieListSerializer()

    class Meta:
        model = UserToMovie
        fields = '__all__'


class UserToMovieUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToMovie
        fields = '__all__'
        read_only_fields = ('id', 'user', 'movie', )
