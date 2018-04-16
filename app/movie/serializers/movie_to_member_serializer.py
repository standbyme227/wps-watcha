from rest_framework import serializers

from actor_director.serializers import MemberNameListSerializer, MemberDefaultListSerializer
from ..models import MovieToMember

__all__ = (
    'MovieToMemberListSerializer'
)

class MovieToMemberListSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='member.name')
    real_name = serializers.ReadOnlyField(source='member.real_name')

    class Meta:
        model = MovieToMember
        fields = (
            'type',
            # 'role_name',
            'member',
            'name',
            'real_name',
        )