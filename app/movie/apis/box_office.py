from rest_framework import (
    authentication,
    filters,
)

from rest_framework.response import Response
from rest_framework.views import APIView

from ..permissions import IsAdminOrReadOnly

from utils.pagination import (
    BoxOfficeRankingPagination,
    BoxOfficeRankingFivePagination,
)
from ..serializers import (
    MovieBoxOfficeRankingSerializer,
)

from ..models import Movie

__all__ = (
    'MovieBoxofficeRankingListView',
    'MovieBoxofficeRankingFiveListView',
)


class MovieBoxofficeRankingListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = BoxOfficeRankingPagination

    # filter_backends = (filters.OrderingFilter,)
    # ordering_fields = ('resource__ticketing_rate',)
    # ordering = ('resource__ticketing_rate',)

    def get(self, request, format=None):
        movie = Movie.objects.filter(ticketing_rate__gte=0.0)
        serializer = MovieBoxOfficeRankingSerializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class MovieBoxofficeRankingFiveListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = BoxOfficeRankingFivePagination

    def get(self, request, format=None):
        movie = Movie.objects.filter(ticketing_rate__gte=0.0)
        serializer = MovieBoxOfficeRankingSerializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
