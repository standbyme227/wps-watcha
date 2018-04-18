from rest_framework import serializers
from movie.serializers.user_to_movie_serializer import UserToMovieWantWatchedListSerializer
from movie.models import Movie, UserToMovie
from movie.serializers import GenreSerializer


__all__ = (
    'WantWatchedMovieListSerializer',
)


class WantWatchedMovieListSerializer(serializers.ModelSerializer):
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
            'poster_image_m',
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
