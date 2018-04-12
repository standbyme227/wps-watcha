from rest_framework import serializers

from ..models import Movie

__all__ = (
    'MovieListSerializer',
)


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
