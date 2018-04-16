from rest_framework import (
    authentication,
)

from rest_framework.response import Response
from rest_framework.views import APIView
from ..permissions import IsAdminOrReadOnly

from utils.pagination import (
    BoxOfficeRankingPagination,
    BoxOfficeRankingFivePagination,
    MovieListDefaultPagination
)
from ..serializers import (
    MovieNameBoxOfficeRankingSerializer,
    MovieBoxOfficeRankingFiveSerializer,
    MovieBoxOfficeRankingSerializer)

from ..models import Movie

__all__ = (
    'MovieBoxofficeRankingNameListView',
    'MovieBoxofficeRankingFiveListView',
    'MovieBoxofficeRankingListView'
)



class MovieBoxofficeRankingNameListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = BoxOfficeRankingPagination

    def get(self, request, format=None):
        movie = Movie.objects.filter(ticketing_rate__gte=0.0)
        movie_list = []
        for item in movie:
            movie_list.append(item)

        serializer = MovieNameBoxOfficeRankingSerializer(movie_list, many=True)
        return Response(serializer.data)












class MovieBoxofficeRankingFiveListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = BoxOfficeRankingFivePagination

    def get(self, request, format=None):
        movie = Movie.objects.filter(ticketing_rate__gte=0.0)
        movie_list = []
        for item in movie:
            movie_list.append(item)

        serializer = MovieBoxOfficeRankingFiveSerializer(movie_list, many=True)
        return Response(serializer.data)


class MovieBoxofficeRankingListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permissions_classes = (IsAdminOrReadOnly,)
    pagination_class = MovieListDefaultPagination

    def get(self, request, format=None):
        movie = Movie.objects.filter(ticketing_rate__gte=0.0)
        movie_list = []
        for item in movie:
            movie_list.append(item)

        serializer = MovieBoxOfficeRankingSerializer(movie_list, many=True)
        return Response(serializer.data)