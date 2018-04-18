from django.urls import path

from ..apis import (
    MovieListView,
    MovieDetailView,
    UserCheckedMovieListView,
    UserCheckedMovieUpdateView,
    UserCheckedMovieCreateView,
    MovieCheckingDataListView,
)

app_name = 'movie'

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('user-checked-movie/', UserCheckedMovieListView.as_view(), name='user-checked-movie-list'),
    path('user-checked-movie/<int:pk>/', UserCheckedMovieUpdateView.as_view(), name='user-checked-movie-update'),
    path('user-checked-movie/create/', UserCheckedMovieCreateView.as_view(), name='user-checked-movie-create'),
    path('<int:pk>/movie-checking-data/', MovieCheckingDataListView.as_view(), name='movie-checking-data'),
]
