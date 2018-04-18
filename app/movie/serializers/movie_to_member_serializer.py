from rest_framework import serializers

from actor_director.serializers import MemberSimpleDetailSerializer
from movie.models import MovieToMember


class MovieToMemberSerializer(serializers.ModelSerializer):
    member = MemberSimpleDetailSerializer()
    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = MovieToMember
        fields = (
            'movie',
            'member',
            'type',
            'role_name',
        )
