from rest_framework import serializers

from movie.serializers.movie_to_member_serializer import MovieToMemberSerializer
from movie.serializers.trailer_youtube_serializer import TrailerYouTubeSerializer
from ..models import Movie, UserToMovie
from ..serializers.genre_serializer import GenreSerializer
from ..serializers.stillcut_serializer import StillCutSerializer
from ..serializers.tag_serializer import TagSerializer
from ..serializers.user_to_movie_serializer import UserToMovieWantWatchedListSerializer, UserToMovieWithUserSerializer

__all__ = (
    'MovieListSerializer',
    'MovieDetailSerializer',
    'MovieSimpleDetailSerializer',
    'WantWatchedMovieListSerializer',
)


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    movie_eval_info = serializers.SerializerMethodField()
    movie_rating_data = serializers.SerializerMethodField()
    still_cuts = StillCutSerializer(many=True)
    genre = GenreSerializer(many=True)
    tag = TagSerializer(many=True)
    trailer_youtube = TrailerYouTubeSerializer(many=True)
    movie_member_list = MovieToMemberSerializer(many=True, read_only=True)

    # interested_user_list = UserToMovieWithUserSerializer(many=True, read_only=True)
    movie_checking_data = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'title_en',
            'd_day',
            'film_rate',
            'running_time',
            'intro',
            'nation',
            'ticketing_rate',
            'audience',
            'rating_avg',
            'movie_eval_info',
            'movie_rating_data',
            'poster_image',
            'still_cuts',
            'genre',
            'tag',
            'trailer_youtube',
            'movie_member_list',
            # 'interested_user_list',
            'movie_checking_data',
        )

    def get_movie_eval_info(self, obj):
        rating_cnt = UserToMovie.objects.filter(movie=obj, rating__isnull=False).count()
        want_movie_cnt = UserToMovie.objects.filter(movie=obj, user_want_movie=True).count()
        comment_cnt = UserToMovie.objects.filter(movie=obj).exclude(comment='').count()
        movie_eval_info = {
            'rating_cnt': rating_cnt,
            'want_movie_cnt': want_movie_cnt,
            'comment_cnt': comment_cnt,
        }
        return movie_eval_info

    def get_movie_rating_data(self, obj):
        items = UserToMovie.objects.filter(movie=obj)
        rating_list = []
        for item in items:
            if item.rating:
                rating_list.append(item.rating)

        # 평점 항목을 추출하기 위한 중복된 값 제거
        remove_duplicate = list(set(rating_list))

        data = {}
        for item in remove_duplicate:
            data[f'{item}'] = rating_list.count(item)
        return data

    def get_movie_checking_data(self, obj):
        queryset = UserToMovie.objects.filter(movie=obj, rating__isnull=False).exclude(comment='').order_by('-modified_date')
        serializer = UserToMovieWithUserSerializer(queryset, many=True, read_only=True)
        return serializer.data


class MovieSimpleDetailSerializer(serializers.ModelSerializer):
    login_user_checked = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'poster_image',
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


class WantWatchedMovieListSerializer(MovieListSerializer):
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
            'poster_image',
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
