from rest_framework import (
    generics,
    authentication,
)

from utils.pagination import (
    MovieListEvalPagination,
)
from ..serializers import (
    MovieMinimumListSerializer, )

from ..models import Movie

__all__ = (
    'MovieEvalListView',
)


class MovieEvalListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieMinimumListSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    pagination_class = MovieListEvalPagination
