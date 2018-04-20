from django.contrib.auth import get_user_model
from rest_framework import permissions, generics
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
        user = self.request.user
        # 유저는 request한 유저 authenticate된 유저로 로그인 상태인 유저이다.
        if self.request.user.interesting_movie_list:
            # 유저의 usertomovie의 오브젝트가 있다면 리스트로 받아온다.
            user_to_movie = UserToMovie.objects.filter(user=user)
            movie_list = []
            for item in user_to_movie:
                movie_list.append(item.movie)
        else:
            movie_list = []
        return movie_list

    def get_serializer_context(self):
        return {'login_user': self.request.user}
