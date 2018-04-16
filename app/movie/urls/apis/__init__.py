from django.urls import path, include

from ...apis import (
    MovieListView,
    UserCheckedMovieListView,
    MovieBoxofficeRankingListView,
    MovieListSerializer,
)

app_name = 'movie'

urlpatterns = [
    path('all/', MovieListSerializer.as_view(), name='movie-list'),
    path('', MovieListView.as_view(), name='movie-list'),
    path('box-office/', MovieBoxofficeRankingListView.as_view(), name='box-office-ranking'),

    path('eval/', include('movie.urls.apis.eval')),
    path('genre/', include('movie.urls.apis.genre')),
    path('tag/', include('movie.urls.apis.tag')),


    path('user-checked-movie/', UserCheckedMovieListView.as_view(), name='user-checked-movie'),
]
