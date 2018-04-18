from rest_framework import serializers
from movie.models import MovieToMember
from .models import Member

__all__ = (
    'MemberDetailSerializer',
    'MemberSimpleDetailSerializer',
    'MemberDefaultListSerializer',
    'MemberNameListSerializer',
)


class MemberDetailSerializer(serializers.ModelSerializer):
    # casting_movie_list = MovieToMemberSerializer(many=True, read_only=True)
    by_director_movie_list = serializers.SerializerMethodField()
    by_main_actor_movie_list = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = (
            'id',
            'name',
            'real_name',
            'img_profile',
            'by_director_movie_list',
            'by_main_actor_movie_list',
        )

    def get_by_director_movie_list(self, obj):
        items = MovieToMember.objects.filter(member=obj, type='1')
        movie_list = []
        for item in items:
            movie_list.append(item.movie)

        from movie.serializers import MovieSimpleDetailSerializer
        serializer = MovieSimpleDetailSerializer(movie_list, many=True, context=self.context)
        return serializer.data

    def get_by_main_actor_movie_list(self, obj):
        items = MovieToMember.objects.filter(member=obj, type='2')
        movie_list = []
        for item in items:
            movie_list.append(item.movie)

        from movie.serializers import MovieSimpleDetailSerializer
        serializer = MovieSimpleDetailSerializer(movie_list, many=True, context=self.context)
        return serializer.data


class MemberSimpleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'id',
            'name',
            'img_profile',
        )


class MemberDefaultListSerializer(serializers.ModelSerializer):
    # type = serializers.ChoiceField(choices=[1])
    class Meta:
        model = Member
        fields = '__all__'


class MemberNameListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = (
            'name',
        )
