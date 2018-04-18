from rest_framework import permissions, status, generics
from rest_framework.response import Response

from members.permissions import IsUserOrReadOnly
from ..models import UserToMovie, Movie
from ..serializers import UserToMovieBasicSerializer


__all__ = (
    'UserCheckedMovieCreateView',
)


class UserCheckedMovieCreateView(generics.CreateAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
        IsUserOrReadOnly,
    )
    queryset = UserToMovie.objects.all()
    serializer_class = UserToMovieBasicSerializer

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        Movie.objects.update_rating_avg(id=self.request.data['movie'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
