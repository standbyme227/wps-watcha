from django.urls import path, include

from ...apis import (
    MovieListView,
    UserCheckedMovieListView,
    UserCheckedMovieUpdateView)

app_name = 'movie'

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('box-office/', include('movie.urls.apis.box_office')),

    path('eval/', include('movie.urls.apis.eval')),
    path('genre/', include('movie.urls.apis.genre')),
    path('tag/', include('movie.urls.apis.tag')),

    path('user-checked-movie/', UserCheckedMovieListView.as_view(), name='user-checked-movie'),
    path('user-checked-movie/<int:pk>/', UserCheckedMovieUpdateView.as_view(), name='user-checked-movie-update'),
]

