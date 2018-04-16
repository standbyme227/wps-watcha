
from ...serializers import GenreSerializer, MovieListSerializer
from ...models import Movie

__all__ = (
    'WantWatchedMovieListSerializer',
)

class WantWatchedMovieListSerializer(MovieListSerializer):
    genre = GenreSerializer(many=True)

    # 장르의 텍스트만 리스트형태로 전달하고 싶을 때에는 아래처럼 SlugRelatedField를 사용
    # genre = serializers.SlugRelatedField(many=True, read_only=True, slug_field='genre')

    class Meta:
        model = Movie
        fields = (
            'id',
            'title_ko',
            'title_en',
            'rating_avg',
            'nation',
            'poster_image',
            'genre',
            'running_time',
        )

