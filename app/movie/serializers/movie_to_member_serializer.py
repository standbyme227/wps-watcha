from rest_framework import serializers

from actor_director.serializers import MemberNameListSerializer
from ..models import MovieToMember

__all__ = (
    'MovieToMemberListSerializer'
)

class MovieToMemberListSerializer(serializers.ModelSerializer):
    # member = MemberNameListSerializer(source='movie_member_list', many=True, read_only=True)
    class Meta:
        model = MovieToMember
        fields = (
            'type',
            'role_name',
            'member',
        )