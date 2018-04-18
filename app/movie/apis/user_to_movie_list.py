from django.contrib.auth import get_user_model
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.pagination import StandardResultSetPagination, SmallResultSetPagination
from ..models import UserToMovie
from ..serializers import UserToMovieBasicSerializer, UserToMovieWithUserSerializer

User = get_user_model()

__all__ = (
    'UserCheckedMovieListView',
    'MovieCheckingDataListView',
)


# class UserCheckedMovieListView(APIView):
#     permission_classes = (
#         permissions.IsAuthenticated,
#     )
#
#     def get(self, request, format=None):
#         # print(request.GET.getlist('pk'))
#         # print(request.query_params.getlist('pk'))
#         movie_list = request.query_params.getlist('pk')
#         user_to_movie = UserToMovie.objects.filter(user=request.user, movie__in=movie_list)
#         if not user_to_movie:
#             data = {"no-data": "does not exist."}
#             return Response(data=data, status=status.HTTP_204_NO_CONTENT)
#         serializer = UserToMovieBasicSerializer(user_to_movie, many=True)
#         return Response(serializer.data)


class UserCheckedMovieListView(generics.ListCreateAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    serializer_class = UserToMovieBasicSerializer
    pagination_class = StandardResultSetPagination

    def get_queryset(self):
        movie_list = self.request.query_params.getlist('pk')
        user_to_movie = UserToMovie.objects.filter(user=self.request.user, movie__in=movie_list)
        return user_to_movie


class MovieCheckingDataListView(generics.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    serializer_class = UserToMovieWithUserSerializer
    pagination_class = SmallResultSetPagination

    def get_queryset(self):
        movie_pk = self.kwargs['pk']
        order = self.request.query_params.get('order', None)
        if order == 'rating_desc':
            order_val = '-rating'
        elif order == 'rating_asc':
            order_val = 'rating'
        else:
            order_val = '-modified_date'
        return UserToMovie.objects.filter(movie=movie_pk, rating__isnull=False).exclude(comment='').order_by(order_val)
