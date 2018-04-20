from rest_framework import serializers

from ..models import StillCut

__all__ = (
    'StillCutSerializer',
)


class StillCutSerializer(serializers.ModelSerializer):
    # movie = serializers.SlugRelatedField(read_only=True, slug_field='title_ko')

    class Meta:
        model = StillCut
        fields = (
            'id',
            'movie',
            'still_img',
            'still_img_x3',
        )
