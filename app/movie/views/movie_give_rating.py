import datetime
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Movie


def artist_like_toggle(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'POST':
        movie.give_rating_user(user=request.user)
        next_path = request.POST.get('next-path', 'artist:artist-list')
        return redirect(next_path)
