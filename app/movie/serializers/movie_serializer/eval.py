from rest_framework import serializers, filters
from ...serializers import GenreSerializer
from ...models import Movie

__all__ = (
    'MovieMinimumListSerializer',
)




class MovieMinimumListSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'poster_image',
            'rating_avg',
            'genre',
            'tag',
        )

#
# class MovieDetailListSerializer(serializers.ModelSerializer):
#     members = MovieToMemberListSerializer(source='movie_member_list', many=True, read_only=True)
#
#     class Meta:
#         model = Movie
#         fields = '__all__'

# class MovieListSerializer(serializers.ModelSerializer):
#     movietomember_set = MovieToMemberListSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Movie
#         fields = (
#             'id',
#             'title_ko',
#             'ticketing_rate',
#             'poster_image',
#             'rating_avg',
#             'movie_created_date',
#             'd_day',
#             'film_rate',
#             'running_time',
#             'intro',
#             'nation',
#             'ticketing_rate',
#             'audience',
#             'poster_image',
#             'rating_avg',
#             'members',
#             'genre',
#             'tag',
#             'modified_date',
#             'created_date',
#             'user',
#         )
