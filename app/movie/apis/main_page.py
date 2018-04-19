from rest_framework import (
    generics,
    authentication,
    permissions)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..permissions import IsAdminOrReadOnly
from utils.pagination import (
    MovieListDefaultPagination,
)
from ..serializers import (
    MovieMinimumListForMainSerializer, )

from ..models import Movie

__all__ = (
    'WatchaRatingTopMovieListView',
    'GenreMovieListView',
    'TagMovieListView',
)

class WatchaRatingTopMovieListView(generics.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    pagination_class = MovieListDefaultPagination
    serializer_class = MovieMinimumListForMainSerializer

    def list(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            movie = Movie.objects.\
                exclude(interested_user_list__id=request.user.pk).filter(rating_avg__gte=4.0).order_by('?')
        else:
            movie = Movie.objects.filter(rating_avg__gte=4.0).order_by('?')
        movie_list = []
        for item in movie:
            movie_list.append(item)

        serializer = MovieMinimumListForMainSerializer(movie_list, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)



class TagMovieListView(generics.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    pagination_class = MovieListDefaultPagination
    serializer_class = MovieMinimumListForMainSerializer
    TAG = ''

    def list(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            movie = Movie.objects.\
                exclude(interested_user_list__id=request.user.pk).filter(tag__tag=self.TAG).order_by('?')
        else:
            movie = Movie.objects.filter(tag__tag=self.TAG).order_by('?')
        movie_list = []
        for item in movie:
            movie_list.append(item)

        serializer = MovieMinimumListForMainSerializer(movie_list, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)


class GenreMovieListView(generics.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    pagination_class = MovieListDefaultPagination
    serializer_class = MovieMinimumListForMainSerializer
    GENRE = ''

    def list(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            movie = Movie.objects.\
                exclude(interested_user_list__id=request.user.pk).filter(genre__genre=self.GENRE).order_by('?')
        else:
            movie = Movie.objects.filter(genre__genre=self.GENRE).order_by('?')
        movie_list = []
        for item in movie:
            movie_list.append(item)

        serializer = MovieMinimumListForMainSerializer(movie_list, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)
