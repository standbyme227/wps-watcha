from rest_framework import (
    generics,
    authentication,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from movie.permissions import IsAdminOrReadOnly
from utils.pagination import (
    MovieListEvalPagination,
)
from ..serializers import (
    MovieMinimumListSerializer, )

from ..models import Movie

__all__ = (
    'EvalTagMovieListView',
    'EvalGenreMovieListView',
)


class EvalTagMovieListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = MovieListEvalPagination

    TAG = ''

    def get(self, request, format=None):
        movie = Movie.objects.filter(tag__tag=self.TAG)
        movie_list = []
        for item in movie:
            movie_list.append(item)

        serializer = MovieMinimumListSerializer(movie_list, many=True)
        return Response(serializer.data)


class EvalGenreMovieListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = MovieListEvalPagination

    GENRE = ''

    def get(self, request, format=None):
        movie = Movie.objects.filter(genre__genre=self.GENRE)
        movie_list = []
        for item in movie:
            movie_list.append(item)

        serializer = MovieMinimumListSerializer(movie_list, many=True)
        return Response(serializer.data)