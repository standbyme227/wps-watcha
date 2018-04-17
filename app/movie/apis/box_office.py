from rest_framework import (
    authentication,
)
from rest_framework.permissions import IsAuthenticated

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
    queryset = Movie.objects.filter(ticketing_rate__gte=0.0)
    serializer_class = MovieNameBoxOfficeRankingSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = BoxOfficeRankingPagination


    def get(self, request):
        if not request.user.is_anonymous:
            queryset = self.queryset.exclude(interested_user_list__token=request.user.token).order_by('-ticketing_rate')
        else:
            queryset = self.queryset.order_by('-ticketing_rate')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


class MovieBoxofficeRankingFiveListView(APIView):
    queryset = Movie.objects.filter(ticketing_rate__gte=0.0)
    serializer_class = MovieBoxOfficeRankingFiveSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = BoxOfficeRankingFivePagination

    def get(self, request):
        if not request.user.is_anonymous:
            queryset = self.queryset.exclude(interested_user_list__token=request.user.token).order_by('-ticketing_rate')
        else:
            queryset = self.queryset.order_by('-ticketing_rate')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer =self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

    # def get(self, request, format=None):
    #     movie = Movie.objects.filter(ticketing_rate__gte=0.0)
    #     movie_list = []
    #     for item in movie:
    #         movie_list.append(item)
    #
    #     serializer = MovieBoxOfficeRankingFiveSerializer(movie_list, many=True)
    #     return Response(serializer.data)


class MovieBoxofficeRankingListView(APIView):
    queryset = Movie.objects.filter(ticketing_rate__gte=0.0)
    serializer_class = MovieBoxOfficeRankingSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = MovieListDefaultPagination

    def get(self, request):
        if not request.user.is_anonymous:
            queryset = self.queryset.exclude(interested_user_list__token=request.user.token).order_by('-ticketing_rate')
        else:
            queryset = self.queryset.order_by('-ticketing_rate')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)

