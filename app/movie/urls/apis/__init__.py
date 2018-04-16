from django.urls import path, include

from ...apis import (
    MovieListView,
    MovieEvalListView,
    UserCheckedMovieListView,
    MovieBoxofficeRankingListView,
    GenreMovieListView,
    TagMovieListView,
    MovieListSerializer,
)

app_name = 'movie'

urlpatterns = [
    path('all/', MovieListSerializer.as_view(), name='movie-list'),
    path('', MovieListView.as_view(), name='movie-list'),
    path('box-office/', MovieBoxofficeRankingListView.as_view(), name='box-office-ranking'),
    path('eval/', MovieEvalListView.as_view(), name='evaluate-movie-list'),

    path('genre/', include('.genre')),
    path('tag/', include('.tag')),

    path('user-checked-movie/', UserCheckedMovieListView.as_view(), name='user-checked-movie'),
]
