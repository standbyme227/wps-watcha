from django.contrib.auth import get_user_model
from rest_framework import permissions, generics
from rest_framework.generics import get_object_or_404
from movie.models import UserToMovie
from movie.serializers.movie_serializer.my_page import WantWatchedMovieListSerializer
from utils.pagination import StandardResultSetPagination


User = get_user_model()

__all__ = (
    'WantWatchedMovieListView',
)


class WantWatchedMovieListView(generics.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    serializer_class = WantWatchedMovieListSerializer
    pagination_class = StandardResultSetPagination

    want_movie = False
    watched_movie = False

    def get_queryset(self):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        if self.want_movie:
            # 보고 싶어요 영화리스트
            user_to_movie = UserToMovie.objects.filter(user=user, user_want_movie=True)
        if self.watched_movie:
            # 봤어요 영화리스트
            user_to_movie = UserToMovie.objects.filter(user=user, user_watched_movie=True)

        movie_list = []
        for item in user_to_movie:
            movie_list.append(item.movie)

        return movie_list

    def get_serializer_context(self):
        return {'login_user': self.request.user}
