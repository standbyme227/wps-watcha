from rest_framework import serializers
from members.serializers.user_serializer import UserMinimumSerializer
from movie.models import UserToMovie

__all__ = (
    'UserToMovieBasicSerializer',
    'UserToMovieUpdateSerializer',
    'UserToMovieWantWatchedListSerializer',
    'UsertoMovieCommentListSerialzier',
)


class UserToMovieBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToMovie
        fields = '__all__'


class UserToMovieUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserToMovie
        fields = '__all__'
        read_only_fields = ('id', 'user', 'movie',)


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


class UsertoMovieCommentListSerialzier(serializers.ModelSerializer):
    user = UserMinimumSerializer(read_only=True, many=True)
    class Meta:
        model = UserToMovie
        fields = (
            'id',
            'comment',
            'user',
        )
