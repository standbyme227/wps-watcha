from rest_framework import serializers

from ..models import Tag

__all__ = (
    'TagSerializer',
)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'tag',
        )
