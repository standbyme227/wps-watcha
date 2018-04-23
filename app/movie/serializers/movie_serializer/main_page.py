from rest_framework import serializers

from movie.serializers.user_to_movie_serializer import UserToMovieWantWatchedListSerializer
from movie.serializers.tag_serializer import TagSerializer
from ...serializers.genre_serializer import GenreSerializer
from ...models import Movie, UserToMovie

__all__ = (
    'MovieListSerializer',
    'MovieMinimumListForMainSerializer',
    'MovieNameBoxOfficeRankingSerializer',
)


class MovieListSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    tag = TagSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'


class MovieMinimumListForMainSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    tag = serializers.CharField(source='get_tag_display', read_only=True)
    login_user_checked = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'movie_created_date',
            'poster_image_m',
            'poster_image_eval_x3',
            'rating_avg',
            'genre',
            'tag',
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

class MovieNameBoxOfficeRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'ticketing_rate',
            'rating_avg',
        )

