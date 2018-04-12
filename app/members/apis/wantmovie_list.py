from django.contrib.auth import get_user_model
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from movie.models import UserToMovie
from ..serializers import UserToMovieSerializer

User = get_user_model()

__all__ = (
    'WantMovieListView',
)


class WantMovieListView(APIView):
    def get(self, request, pk, format=None):
        user = get_object_or_404(User, pk=pk)
        print(f'user: {user}')
        # user_to_movie = UserToMovie.objects.filter(user__pk=user.pk)
        user_to_movie = UserToMovie.objects.filter(user=user, user_want_movie=True)

        serializer = UserToMovieSerializer(user_to_movie, many=True)
        return Response(serializer.data)
