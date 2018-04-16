from django.urls import path

from ..apis import (
    MovieListView,
    MovieEvalListView,
    UserCheckedMovieListView,
    MovieBoxofficeRankingListView,
)

app_name = 'movie'

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('box-office/', MovieBoxofficeRankingListView.as_view(), name='box-office-ranking'),
    path('eval/', MovieEvalListView.as_view(), name='evaluate-movie-list'),
    path('user-checked-movie/', UserCheckedMovieListView.as_view(), name='user-checked-movie')
]
