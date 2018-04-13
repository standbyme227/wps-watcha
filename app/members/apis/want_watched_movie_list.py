from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from movie.models import UserToMovie
from movie.serializers import WantWatchedMovieListSerializer


User = get_user_model()

__all__ = (
    'WantWatchedMovieListView',
)


class WantWatchedMovieListView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    want_movie = False
    watched_movie = False

    def get(self, request, pk, format=None):
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

        serializer = WantWatchedMovieListSerializer(movie_list, many=True)
        return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     if request.data['user_want_movie'] == request.data['user_watched_movie']:
    #         err = {"error": ["user_want_movie' 와 'user_watched_movie'의 value는 둘 다 '참'이거나 '거짓'일 수 없습니다."]}
    #         return Response(data=err, status=status.HTTP_400_BAD_REQUEST)
    #
    #     user = get_object_or_404(User, pk=pk)
    #     user_to_movie = get_object_or_404(UserToMovie, user=user, movie=request.data['movie'])
    #     serializer = UserToMovieUpdateSerializer(user_to_movie, data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
