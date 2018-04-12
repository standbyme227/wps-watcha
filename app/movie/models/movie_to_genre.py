from django.db import models
from ..models import Movie, Genre

__all__ = (
    'MovieToGenre',
)


class MovieToGenre(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_genre_list', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, related_name='genre_movie_list', on_delete=models.CASCADE)

    def __str__(self):
        return f'movie: {self.movie}, genre: {self.genre}'
