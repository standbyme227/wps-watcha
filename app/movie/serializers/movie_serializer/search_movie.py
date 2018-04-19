from rest_framework import serializers

from ...models import Movie, MovieToMember

__all__ = (
    'MovieSearchResultSerializer',
)


class MovieSearchResultSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()
    main_actor = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'title_en',
            'movie_created_date',
            'poster_image',
            'director',
            'main_actor',
        )

    def get_director(self, obj):
        movie_to_member = MovieToMember.objects.filter(movie=obj, type='1').prefetch_related('member')
        director_list = []
        for item in movie_to_member:
            director_list.append(item.member.name)
        return ','.join(director_list)

    def get_main_actor(self, obj):
        movie_to_member = MovieToMember.objects.filter(movie=obj, type='2').prefetch_related('member')
        actor_list = []
        for item in movie_to_member:
            actor_list.append(item.member.name)
        return ','.join(actor_list)
