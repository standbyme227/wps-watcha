
from rest_framework import (
    generics,
    authentication,
)


from utils.pagination import (
    MovieListDefaultPagination,
)
from ..serializers import (
    MovieMinimumListSerializer, MovieListSerializer)

from ..models import Movie

__all__ = (
    'MovieListView',
)

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieMinimumListSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    pagination_class = MovieListDefaultPagination