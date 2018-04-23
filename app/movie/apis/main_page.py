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

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            movie = Movie.objects.\
                exclude(interested_user_list__user_id=self.request.user.pk).filter(rating_avg__gte=4.0).order_by('?')
        else:
            movie = Movie.objects.filter(rating_avg__gte=4.0).order_by('?')
        return movie

    def get_serializer_context(self):
        return {'login_user': self.request.user}

class TagMovieListView(generics.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    pagination_class = MovieListDefaultPagination
    serializer_class = MovieMinimumListForMainSerializer
    TAG = ''

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            movie = Movie.objects.\
                exclude(interested_user_list__user_id=self.request.user.pk).filter(tag__tag=self.TAG).order_by('?')
        else:
            movie = Movie.objects.filter(tag__tag=self.Tag).order_by('?')
        return movie

    def get_serializer_context(self):
        return {'login_user': self.request.user}

class GenreMovieListView(generics.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    pagination_class = MovieListDefaultPagination
    serializer_class = MovieMinimumListForMainSerializer
    GENRE = ''

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            movie = Movie.objects.\
                exclude(interested_user_list__user_id=self.request.user.pk).filter(genre__genre=self.GENRE).order_by('?')
        else:
            movie = Movie.objects.filter(tag__tag=self.Tag).order_by('?')
        return movie

    def get_serializer_context(self):
        return {'login_user': self.request.user}