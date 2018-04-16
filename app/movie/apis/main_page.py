from rest_framework import (
    generics,
    authentication,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from ..permissions import IsAdminOrReadOnly
from utils.pagination import (
    MovieListDefaultPagination,
)
from ..serializers import (
    MovieMinimumListSerializer, )

from ..models import Movie

__all__ = (
    'WatchaRatingTopMovieListView',
    'GenreMovieListView',
    'TagMovieListView',
)


class WatchaRatingTopMovieListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = MovieListDefaultPagination

    def get(self, request, format=None):
        movie = Movie.objects.filter(rating_avg__gte=4.3)
        serializer = MovieMinimumListSerializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class TagMovieListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = MovieListDefaultPagination

    TAG = ''

    def get(self, request, format=None):
        movie = Movie.objects.filter(tag__tag=self.TAG)
        movie_list = []
        for item in movie:
            movie_list.append(item)

        serializer = MovieMinimumListSerializer(movie_list, many=True)
        return Response(serializer.data)


class GenreMovieListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = MovieListDefaultPagination

    GENRE = ''

    def get(self, request, format=None):
        movie = Movie.objects.filter(genre__genre=self.GENRE)
        movie_list = []
        for item in movie:
            movie_list.append(item)

        serializer = MovieMinimumListSerializer(movie_list, many=True)
        return Response(serializer.data)
