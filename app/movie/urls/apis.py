from django.urls import path

from ..apis import (
    MovieListView,
    UserCheckedMovieListView,
)

app_name = 'movie'

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('user-checked-movie/', UserCheckedMovieListView.as_view(), name='user-checked-movie')
]
