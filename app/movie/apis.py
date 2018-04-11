from rest_framework import generics

from .serializer import MovieSerializer
from .models import Movie


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
