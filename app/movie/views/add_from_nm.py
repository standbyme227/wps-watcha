from django.shortcuts import render, redirect

from ..models import Movie

__all__ = (
    'movie_add_from_naver',
)


def movie_add_from_naver(request):
    if request.method == 'POST':
        naver_movie_id = request.POST['naver_movie_id']
        Movie.objects.update_or_create_from_naver(naver_movie_id)

        return redirect('movie:movie-list')
