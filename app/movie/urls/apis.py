from django.urls import path

from ..apis import (
    MovieListView,
    UserCheckedMovieListView,
    UserCheckedMovieUpdateView,
)

app_name = 'movie'

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('user-checked-movie/', UserCheckedMovieListView.as_view(), name='user-checked-movie-list'),
    path('user-checked-movie/update/', UserCheckedMovieUpdateView.as_view(), name='user-checked-movie-update'),
]
