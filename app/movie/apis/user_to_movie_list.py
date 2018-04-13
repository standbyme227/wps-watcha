from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import UserToMovie
from ..serializers import UserToMovieBasicSerializer

User = get_user_model()

__all__ = (
    'UserCheckedMovieListView',
)


class UserCheckedMovieListView(APIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def post(self, request, format=None):
        movie_list = []
        for item in request.data['movie-list']:
            movie_list.append(item['id'])
        user_to_movie = UserToMovie.objects.filter(user=request.user, movie__in=movie_list)
        if not user_to_movie:
            data = {"no-data": "does not exist."}
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)
        serializer = UserToMovieBasicSerializer(user_to_movie, many=True)
        return Response(serializer.data)
