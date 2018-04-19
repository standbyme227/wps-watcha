from django.db.models import Q
from rest_framework import generics, permissions, filters

from movie.models import Movie
from movie.serializers import MovieListSerializer
from utils.pagination import StandardResultSetPagination


class SearchMovieListView(generics.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = MovieListSerializer
    pagination_class = StandardResultSetPagination

    # SearchFilter 를 사용하면 search 기능을 쉽게 구현 할 수 있음.
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('title_ko', 'title_en', 'intro', 'interested_user_list__comment')

    def get_queryset(self):
        try:
            if self.request.query_params['movie']:
                val = self.request.query_params['movie']
                return Movie.objects.filter(Q(title_ko__contains=val) | Q(title_en__contains=val))
            return Movie.objects.none()
        except:
            return Movie.objects.none()
