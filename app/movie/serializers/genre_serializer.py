from rest_framework import serializers

from ..models import Genre

__all__ = (
    'GenreSerializer',
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
