from rest_framework import serializers
from ..models import MovieToMember
from actor_director.serializers import MemberNameListSerializer, MemberDefaultListSerializer

__all__ = (
    'MovieToMemberListSerializer'
)


class MovieToMemberListSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='member.name')
    real_name = serializers.ReadOnlyField(source='member.real_name')
    type = serializers.CharField(source='get_type_display', read_only=True)
    # type = serializers.CharField(choices=MovieToMember.CHOICES_MEMBER_TYPE)
    class Meta:
        model = MovieToMember
        fields = (
            'type',
            # 'role_name',
            'member',
            'name',
            'real_name',
        )
