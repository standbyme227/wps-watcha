from rest_framework import serializers

from ..models import Movie

__all__ = (
    'MovieSerializer',
)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
