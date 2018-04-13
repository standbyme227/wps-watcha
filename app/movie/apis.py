from rest_framework import generics

from .serializers import MovieListSerializer
from .models import Movie


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
