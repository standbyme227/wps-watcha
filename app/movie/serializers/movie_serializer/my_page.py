# from django.contrib.auth import get_user_model
from rest_framework import serializers
from movie.serializers.user_to_movie_serializer import UserToMovieWantWatchedListSerializer
from movie.models import Movie, UserToMovie
from movie.serializers import GenreSerializer

__all__ = (
    'WantWatchedMovieListSerializer',
    'MovieMinimumListForMySerializer',
    'CommentedMovieListSerializer',
    'MovieNationListSerializer',
)

# User = get_user_model()
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
            'poster_image_my_x3',
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


class MovieMinimumListForMySerializer(serializers.ModelSerializer):
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
            'nation',
        )


class CommentedMovieListSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    commented_user = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'title_en',
            'nation',
            'poster_image_m',
            'poster_image_my_x3',
            'genre',
            'running_time',
            'commented_user',
        )


    def get_commented_user(self, obj):
        if UserToMovie.objects.filter(user=self.context['user'], movie=obj):
            items = UserToMovie.objects.filter(user=self.context['user'], movie=obj)
            # UserToMovie에서 유저는 login한 User
            if len(items) == 1:
                # 한 유저가 평가한 그 영화는 하나, 대신 list 형태로 나올테니 len을 확인한다.
                for item in items:
                    serializer = UserToMovieWantWatchedListSerializer(item)
                    return serializer.data
            elif len(items) == 0:
                return {'no-data': 'does not exist.'}
            else:
                return {'error': 'Problems with data consistency'}


class MovieNationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'nation',
        )