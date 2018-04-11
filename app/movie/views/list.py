from django.shortcuts import render
from movie.models import Movie

__all__ = (
    'movie_list',
)


def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movie/movie_list.html', context)

