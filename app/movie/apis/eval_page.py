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
        if not request.user.is_anonymous:
            movie = Movie.objects.\
                exclude(interested_user_list__token=request.user.token).filter(tag__tag=self.TAG).order_by('?')
        else:
            movie = Movie.objects.filter(tag__tag=self.TAG).order_by('?')
        # movie = Movie.objects.filter(tag__tag=self.TAG)
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
        if not request.user.is_anonymous:
            movie = Movie.objects.\
                exclude(interested_user_list__token=request.user.token).filter(genre__genre=self.GENRE).order_by('?')
        else:
            movie = Movie.objects.filter(genre__genre=self.GENRE).order_by('?')
        # movie = Movie.objects.filter(genre__genre=self.GENRE)
        movie_list = []
        for item in movie:
            movie_list.append(item)

        serializer = MovieMinimumListSerializer(movie_list, many=True)
        return Response(serializer.data)