from rest_framework import serializers
from django.contrib.auth import get_user_model

# from movie.models import UserToMovie

User = get_user_model()

__all__ = (
    # 'UserToMovieSerializer',
    'UserSerializer',
    'UserDetailSerializer',
    'UserEmailSerializer',
)


# class UserToMovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserToMovie
#         fields = (
#             'movie',
#             'user_want_movie',
#             'user_watched_movie',
#             'rating',
#             'comment'
#         )
#
#
# class UserSerializer(serializers.ModelSerializer):
#     interesting_movie_list = UserToMovieSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = User
#         fields = (
#             'pk',
#             'email',
#             'username',
#             'nickname',
#             'img_profile',
#             'first_name',
#             'last_name',
#             'interesting_movie_list'
#         )
#         read_only_fields = ('pk', 'username',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'username',
            'nickname',
            'img_profile',
            'first_name',
            'last_name',
        )
        read_only_fields = ('pk', 'username',)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'username',
            'nickname',
            'img_profile',
            'first_name',
            'last_name',
        )
        read_only_fields = ('pk', 'username', 'email',)


class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'username',
        )
        read_only_fields = ('pk', 'username',)