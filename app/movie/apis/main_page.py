
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
    MovieMinimumListSerializer,)

from ..models import Movie

__all__ = (
    'WatchaRatingTopMovieListView',
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

class TopMovieInKoreaListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = MovieListDefaultPagination

    def get(self, request, format=None):
        movie = Movie.objects.filter(tag__tag='국내 누적관객수 TOP 영화')
        serializer = MovieMinimumListSerializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

class TopAudienceMovieListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = MovieListDefaultPagination

    def get(self, request, format=None):
        movie = Movie.objects.filter(tag__tag='역대 100만 관객 돌파 영화')
        serializer = MovieMinimumListSerializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

class TopMovieInTheWorldListView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = MovieListDefaultPagination

    def get(self, request, format=None):
        movie = Movie.objects.filter(tag__tag='전세계 흥행 TOP 영화')
        serializer = MovieMinimumListSerializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

class HeroMovieListView:
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = MovieListDefaultPagination

    def get(self, request, format=None):
        movie = Movie.objects.filter(tag__tag='슈퍼 히어로 영화')
        serializer = MovieMinimumListSerializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

class SportsMovieListView:
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = MovieListDefaultPagination

    def get(self, request, format=None):
        movie = Movie.objects.filter(tag__tag='스포츠 영화')
        serializer = MovieMinimumListSerializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

# class GenreMovieListView:
#     authentication_classes = (authentication.TokenAuthentication,)
#     permission_classes = (IsAdminOrReadOnly,)
#     pagination_class = MovieListDefaultPagination
#
#     def get(self, request, format=None):
#         genre =

