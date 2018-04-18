from django.contrib.auth import get_user_model
from rest_framework import serializers

from members.serializers.user_serializer import UserSimpleDetailSerializer
from ..models import UserToMovie

User = get_user_model()

__all__ = (
    'UserToMovieBasicSerializer',
    'UserToMovieWithUserSerializer',
    'UserToMovieUpdateSerializer',
    'UserToMovieWantWatchedListSerializer',
)


class UserToMovieBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToMovie
        fields = '__all__'


class UserToMovieWithUserSerializer(serializers.ModelSerializer):
    user = UserSimpleDetailSerializer(read_only=True)

    class Meta:
        model = UserToMovie
        fields = (
            'id',
            'user_want_movie',
            'user_watched_movie',
            'rating',
            'comment',
            'modified_date',
            'user',
            'movie',
        )


# class UserToMovieIncludeMovieInfoSerializer(serializers.ModelSerializer):
#     movie = WantWatchedMovieListSerializer()
#
#     class Meta:
#         model = UserToMovie
#         fields = '__all__'


class UserToMovieUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToMovie
        fields = '__all__'
        read_only_fields = ('id', 'user', 'movie', )


class UserToMovieWantWatchedListSerializer(serializers.ModelSerializer):
    # login_user_id = serializers.IntegerField(source='user')

    class Meta:
        model = UserToMovie
        fields = (
            'id',
            'user_want_movie',
            'user_watched_movie',
            'rating',
            'comment',
            'user',
            'movie',
        )
