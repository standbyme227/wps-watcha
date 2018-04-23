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

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            movie = Movie.objects. \
                exclude(interested_user_list__user_id=self.request.user.pk).filter(rating_avg__gte=4.0).order_by('?')
        else:
            movie = Movie.objects.filter(rating_avg__gte=4.0).order_by('?')
        return movie
        # movie_list = []
        # for item in movie:
        #     movie_list.append(item)
        # return movie_list
        # 리스트를 반환해야 되는줄 알았다.
    def get_serializer_context(self):
        return {'login_user': self.request.user}

class EvalTagMovieListView(generics.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    pagination_class = MovieListEvalPagination
    serializer_class = MovieMinimumListForMainSerializer
    TAG = ''

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            movie = Movie.objects. \
                exclude(interested_user_list__user_id=self.request.user.pk).filter(tag__tag=self.TAG).order_by('?')
        else:
            movie = Movie.objects.filter(tag__tag=self.TAG).order_by('?')
        # movie = Movie.objects.filter(tag__tag=self.TAG)
        return movie

    def get_serializer_context(self):
        return {'login_user': self.request.user}



class EvalGenreMovieListView(generics.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    pagination_class = MovieListEvalPagination
    serializer_class = MovieMinimumListForMainSerializer

    GENRE = ''

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            movie = Movie.objects. \
                exclude(interested_user_list__user_id=self.request.user.pk).filter(genre__genre=self.GENRE).order_by('?')
        else:
            movie = Movie.objects.filter(genre__genre=self.GENRE).order_by('?')
        return movie

    def get_serializer_context(self):
        return {'login_user': self.request.user}



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