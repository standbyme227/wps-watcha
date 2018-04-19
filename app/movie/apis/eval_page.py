from rest_framework import (
    generics,
    authentication,
    permissions)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from movie.permissions import IsAdminOrReadOnly
from utils.pagination import (
    MovieListEvalPagination,
)
from ..serializers import (
    MovieMinimumListForMainSerializer, )

from ..models import Movie

__all__ = (
    'EvalWatchaRatingTopMovieListView',
    'EvalTagMovieListView',
    'EvalGenreMovieListView',
)


class EvalWatchaRatingTopMovieListView(generics.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    pagination_class = MovieListEvalPagination
    serializer_class = MovieMinimumListForMainSerializer
    # get_query_set으로 수정.
    # 주말동안
    def list(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            movie = Movie.objects. \
                exclude(interested_user_list__id=request.user.pk).filter(rating_avg__gte=4.3).order_by('?')
        else:
            movie = Movie.objects.filter(rating_avg__gte=4.3).order_by('?')
        movie_list = []
        for item in movie:
            movie_list.append(item)
        serializer = MovieMinimumListForMainSerializer(movie_list, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)


class EvalTagMovieListView(generics.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    pagination_class = MovieListEvalPagination
    serializer_class = MovieMinimumListForMainSerializer
    TAG = ''

    def list(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            movie = Movie.objects. \
                exclude(interested_user_list__id=request.user.pk).filter(tag__tag=self.TAG).order_by('?')
        else:
            movie = Movie.objects.filter(tag__tag=self.TAG).order_by('?')
        # movie = Movie.objects.filter(tag__tag=self.TAG)
        movie_list = []
        for item in movie:
            movie_list.append(item)

        serializer = MovieMinimumListForMainSerializer(movie_list, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)


class EvalGenreMovieListView(generics.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    pagination_class = MovieListEvalPagination
    serializer_class = MovieMinimumListForMainSerializer

    GENRE = ''

    def list(self, request, *arg, **kwargs):
        if not request.user.is_anonymous:
            movie = Movie.objects. \
                exclude(interested_user_list__id=request.user.pk).filter(genre__genre=self.GENRE).order_by('?')
        else:
            movie = Movie.objects.filter(genre__genre=self.GENRE).order_by('?')
        movie_list = []
        for item in movie:
            movie_list.append(item)

        serializer = MovieMinimumListForMainSerializer(movie_list, many=True)
        page = self.paginate_queryset(serializer.data)
        # queryset = serializer.data
        return self.get_paginated_response(page)




# class EvalWatchaRatingTopMovieListView(APIView):
#     authentication_classes = (authentication.TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     pagination_class = MovieListEvalPagination
#
#     def get(self, request, format=None):
#         if not request.user.is_anonymous:
#             movie = Movie.objects. \
#                 exclude(interested_user_list__id=request.user.pk).filter(rating_avg__gte=4.3).order_by('?')
#         else:
#             movie = Movie.objects.filter(rating_avg__gte=4.3).order_by('?')
#         movie_list = []
#         for item in movie:
#             movie_list.append(item)
#
#         serializer = MovieMinimumListSerializer(movie_list, many=True)
#         return Response(serializer.data)