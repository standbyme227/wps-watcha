from rest_framework import (
    authentication,
    generics, permissions)
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView
from ..permissions import IsAdminOrReadOnly

from utils.pagination import (
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


# class EvalWatchaRatingTopMovieListView(generics.ListAPIView):
#     permission_classes = (
#         permissions.IsAuthenticated,
#     )
#     pagination_class = MovieListEvalPagination
#     serializer_class = MovieMinimumListForMainSerializer
#
#     # get_query_set으로 수정.
#     # 주말동안
#
#     def get_queryset(self):
#         if not self.request.user.is_anonymous:
#             movie = Movie.objects. \
#                 exclude(interested_user_list__user_id=self.request.user.pk).filter(rating_avg__gte=4.0).order_by('?')
#         else:
#             movie = Movie.objects.filter(rating_avg__gte=4.0).order_by('?')
#         return movie


class MovieBoxofficeRankingNameListView(generics.ListAPIView):
    serializer_class = MovieNameBoxOfficeRankingSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            movie = Movie.objects.filter(ticketing_rate__gte=0.0).order_by('-ticketing_rate')
        return movie


class MovieBoxofficeRankingFiveListView(generics.ListAPIView):
    serializer_class = MovieBoxOfficeRankingFiveSerializer
    pagination_class = MovieListDefaultPagination
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            movie = Movie.objects.filter(ticketing_rate__gte=0.0).order_by('-ticketing_rate')
        return movie

    def get_serializer_context(self):
        return {'login_user': self.request.user}


class MovieBoxofficeRankingListView(generics.ListAPIView):
    serializer_class = MovieBoxOfficeRankingSerializer
    pagination_class = MovieListDefaultPagination
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            movie = Movie.objects.filter(ticketing_rate__gte=0.0).order_by('-ticketing_rate')
        return movie

    def get_serializer_context(self):
        return {'login_user': self.request.user}

# class MovieBoxofficeRankingFiveListView(APIView):
#     queryset = Movie.objects.filter(ticketing_rate__gte=0.0)
#     serializer_class = MovieBoxOfficeRankingFiveSerializer
#     authentication_classes = (authentication.TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     pagination_class = MovieListDefaultPagination
#
#     def get(self, request):
#         if not request.user.is_anonymous:
#             queryset = self.queryset.order_by('-ticketing_rate')
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.serializer_class(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#     @property
#     def paginator(self):
#         if not hasattr(self, '_paginator'):
#             if self.pagination_class is None:
#                 self._paginator = None
#             else:
#                 self._paginator = self.pagination_class()
#         return self._paginator
#
#     def paginate_queryset(self, queryset):
#         if self.paginator is None:
#             return None
#         return self.paginator.paginate_queryset(queryset, self.request, view=self)
#
#     def get_paginated_response(self, data):
#         assert self.paginator is not None
#         return self.paginator.get_paginated_response(data)
#
#     # def get(self, request, format=None):
#     #     movie = Movie.objects.filter(ticketing_rate__gte=0.0)
#     #     movie_list = []
#     #     for item in movie:
#     #         movie_list.append(item)
#     #
#     #     serializer = MovieBoxOfficeRankingFiveSerializer(movie_list, many=True)
#     #     return Response(serializer.data)
