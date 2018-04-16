from django.contrib.auth import get_user_model
from rest_framework import permissions, status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from members.permissions import IsUserOrReadOnly
from ..models import UserToMovie, Movie
from ..serializers import UserToMovieUpdateSerializer

User = get_user_model()

__all__ = (
    'UserCheckedMovieUpdateView',
)


# class UserCheckedMovieUpdateView(APIView):
#     permission_classes = (
#         permissions.IsAuthenticated,
#     )
#
#     def put(self, request, format=None):
#         if request.data['user_want_movie'] == request.data['user_watched_movie']:
#             err = {"error": ["user_want_movie' 와 'user_watched_movie'의 value는 둘 다 '참'이거나 '거짓'일 수 없습니다."]}
#             return Response(data=err, status=status.HTTP_400_BAD_REQUEST)
#
#         # user = get_object_or_404(User, user=)
#         user_to_movie = get_object_or_404(UserToMovie, user=request.user, movie=request.data['movie'])
#         serializer = UserToMovieUpdateSerializer(user_to_movie, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             # movie = get_object_or_404(Movie, pk=request.data['movie'])
#             Movie.objects.update_rating_avg(id=request.data['movie'])
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCheckedMovieUpdateView(generics.UpdateAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
        IsUserOrReadOnly,
    )
    queryset = UserToMovie.objects.all()
    serializer_class = UserToMovieUpdateSerializer

    def perform_update(self, serializer):
        serializer.save()
        Movie.objects.update_rating_avg(id=self.request.data['movie'])
