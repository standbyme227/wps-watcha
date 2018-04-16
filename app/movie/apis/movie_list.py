
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
    'MovieListSerializer',
)

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieMinimumListSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    pagination_class = MovieListDefaultPagination

class MovieListSerializer(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    pagination_class = MovieListDefaultPagination