# from django.contrib.auth import get_user_model
# from rest_framework import generics
#
# from utils.pagination import SmallResultSetPagination
# from ..serializers import UserSerializer
#
# User = get_user_model()
#
# __all__ = (
#     'MovieListView',
# )
#
#
# class MovieListView(generics.ListAPIView):
#     queryset = User.objects.filter(is_active=True, is_staff=False, is_superuser=False)
#     serializer_class = UserSerializer
#     pagination_class = SmallResultSetPagination
from rest_framework import generics

from ..serializer import MovieSerializer
from ..models import Movie


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
