from django.contrib.auth import get_user_model
from rest_framework import permissions, generics
from rest_framework.generics import get_object_or_404

from movie.models import UserToMovie
from movie.serializers.movie_serializer.my_page import CommentedMovieListSerializer
from utils.pagination import StandardResultSetPagination

User = get_user_model()

__all__ = (
    'CommentedMovieListView',
)


class CommentedMovieListView(generics.ListAPIView):
    permissions_classes = (
        permissions.IsAuthenticated
    )
    # 토큰으로 인증된 사용자만 허용

    serializer_class = CommentedMovieListSerializer
    pagination_class = StandardResultSetPagination

    # comment = ''

    def get_queryset(self):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        if user.interesting_movie_list:
            # 유저의 usertomovie의 오브젝트가 있다면 리스트로 받아온다.
            user_to_movie = UserToMovie.objects.filter(user=user)
            movie_list = []
            for item in user_to_movie:
                movie_list.append(item.movie)
        else:
            movie_list = []
        return movie_list

    def get_serializer_context(self):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        return {'user': user}
