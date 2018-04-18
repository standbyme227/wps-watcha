from rest_framework import serializers

from ..models import TrailerYouTube

__all__ = (
    'TrailerYouTubeSerializer',
)


class TrailerYouTubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrailerYouTube
        fields = (
            'title',
            'url_thumbnail',
            'get_trailer_url',
        )
