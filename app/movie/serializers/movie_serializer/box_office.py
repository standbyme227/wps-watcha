from rest_framework import serializers

from movie.serializers.user_to_movie_serializer import UserToMovieCommentSerializer
from movie.serializers.movie_to_member_serializer import MovieToMemberListSerializer
from ...serializers.genre_serializer import GenreSerializer
from ...models import Movie, UserToMovie

__all__ = (
    'MovieMinimumListForBoxSerializer',
    'MovieNameBoxOfficeRankingSerializer',
    'MovieBoxOfficeRankingFiveSerializer',
    'MovieBoxOfficeRankingSerializer',

)


class MovieMinimumListForBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'poster_image_m',
            'rating_avg',
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


class MovieBoxOfficeRankingFiveSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    film_rate = serializers.CharField(source='get_film_rate_display', read_only=True)
    comment = serializers.SerializerMethodField(read_only=True, default=None)
    username = serializers.SerializerMethodField(read_only=True, default=None)
    img_profile = serializers.SerializerMethodField(read_only=True, default=None)
    user_pk = serializers.SerializerMethodField(read_only=True, default=None)
    # user = serializers.SerializerMethodField(read_only=True)
    # user = UserToMovieCommentSerializer(read_only=True)
    # user = UserToMovieCommentSerializer(source='interested_user_list', many=True, read_only=True)
    # user = UserMinimumSerializer(read_only=True, many=True)
    # user = serializers.ReadOnlyField(source='movie.interested_user_list')
    # comment = UserToMovieCommentSerializer(read_only=True)
    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'movie_created_date',
            'ticketing_rate',
            'rating_avg',
            'poster_image',
            'poster_image_m',
            'd_day',
            'audience',
            'film_rate',
            'running_time',
            'genre',
            'username',
            'comment',
            'img_profile',
            'user_pk',
        )

    def get_user_pk(self, obj):
        user_to_movie = obj.interested_user_list.all().first()
        if not user_to_movie == None:
            user_pk = user_to_movie.user.pk
        else:
            user_pk = None
        return user_pk

    def get_comment(self, obj):
        user_to_movie = obj.interested_user_list.all().first()
        if not user_to_movie == None:
            comment = user_to_movie.comment
        else:
            comment = None
        return comment

    def get_username(self, obj):
        user_to_movie = obj.interested_user_list.all().first()
        if not user_to_movie == None:
            username = user_to_movie.user.nickname
        else:
            username = None
        return username

    def get_img_profile(self, obj):
        user_to_movie = obj.interested_user_list.all().first()
        if not user_to_movie == None:
            img_profile_is = user_to_movie.user.img_profile
        else:
            img_profile_is = None
        if img_profile_is:
            img_profile = img_profile_is.url
        else:
            img_profile = None
        return img_profile

    # def get_user(self, obj):
    #     user = obj.interested_user_list.all().last()
    #     return user


class MovieBoxOfficeRankingSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    members = MovieToMemberListSerializer(source='movie_member_list', many=True, read_only=True)
    film_rate = serializers.CharField(source='get_type_display', read_only=True)
    comment = serializers.SerializerMethodField(read_only=True, default=None)
    username = serializers.SerializerMethodField(read_only=True, default=None)
    img_profile = serializers.SerializerMethodField(read_only=True, default=None)
    user_pk = serializers.SerializerMethodField(read_only=True, default=None)
    want_count = serializers.SerializerMethodField(read_only=True, default=None)
    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'ticketing_rate',
            'rating_avg',
            'poster_image_m',
            'poster_image_box_x3',
            'members',
            'd_day',
            'audience',
            'film_rate',
            'running_time',
            'genre',
            'user_pk',
            'username',
            'img_profile',
            'comment',
            'want_count',
        )
    def get_user_pk(self, obj):
        user_to_movie = obj.interested_user_list.all().first()
        if not user_to_movie == None:
            user_pk = user_to_movie.user.pk
        else:
            user_pk = None
        return user_pk

    def get_comment(self, obj):
        user_to_movie = obj.interested_user_list.all().first()
        if not user_to_movie == None:
            comment = user_to_movie.comment
        else:
            comment = None
        return comment

    def get_username(self, obj):
        user_to_movie = obj.interested_user_list.all().first()
        if not user_to_movie == None:
            username = user_to_movie.user.nickname
        else:
            username = None
        return username

    def get_img_profile(self, obj):
        user_to_movie = obj.interested_user_list.all().first()
        if not user_to_movie == None:
            img_profile_is = user_to_movie.user.img_profile
        else:
            img_profile_is = None
        if img_profile_is:
            img_profile = img_profile_is.url
        else:
            img_profile = None
        return img_profile

    def get_want_count(self, obj):
        user_to_movie = obj.interested_user_list
        if not user_to_movie == None:
            want_movie = user_to_movie.filter(user_want_movie=True)
            want_count = want_movie.count()
        else:
            want_count = 0
        return want_count