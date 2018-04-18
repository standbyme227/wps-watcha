from rest_framework import generics, permissions

from movie.models import Movie
from movie.serializers import MovieDetailSerializer


class MovieDetailView(generics.RetrieveAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

    def get_serializer_context(self):
        print('url의 pk값: ', self.kwargs['pk'])  # url의 pk값 출력하기
        return {'login_user': self.request.user}
