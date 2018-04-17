from django.urls import path

from ....apis import (
    EvalGenreMovieListView,
)

app_name = 'eval-genre'

urlpatterns = [
    path('action/', EvalGenreMovieListView.as_view(GENRE='액션'), name='action-movie-list'),
    path('crime/', EvalGenreMovieListView.as_view(GENRE='범죄'), name='crime-movie-list'),
    path('drama/', EvalGenreMovieListView.as_view(GENRE='드라마'), name='drama-movie-list'),
    path('comedy/', EvalGenreMovieListView.as_view(GENRE='코미디'), name='comedy-movie-list'),
    path('romance/', EvalGenreMovieListView.as_view(GENRE='로맨스/멜로'), name='romance-movie-list'),
    path('thriller/', EvalGenreMovieListView.as_view(GENRE='스릴러'), name='thriller-movie-list'),
    path('roco/', EvalGenreMovieListView.as_view(GENRE='로맨틱코미디'), name='roco-movie-list'),
    path('war/', EvalGenreMovieListView.as_view(GENRE='전쟁'), name='war-movie-list'),
    path('fantasy/', EvalGenreMovieListView.as_view(GENRE='판타지'), name='fantasy-movie-list'),
    path('sf/', EvalGenreMovieListView.as_view(GENRE='SF'), name='sf-movie-list'),
    path('animation/', EvalGenreMovieListView.as_view(GENRE='애니메이션'), name='animation-movie-list'),
    path('documentary/', EvalGenreMovieListView.as_view(GENRE='다큐멘터리'), name='documentary-movie-list'),
    path('horror/', EvalGenreMovieListView.as_view(GENRE='공포'), name='horror-movie-list'),
    path('western/', EvalGenreMovieListView.as_view(GENRE='서부'), name='western-movie-list'),
    path('musical/', EvalGenreMovieListView.as_view(GENRE='뮤지컬'), name='musical-movie-list'),
    path('martial-arts/', EvalGenreMovieListView.as_view(GENRE='무협'), name='martial-arts-movie-list'),
    path('mistery/', EvalGenreMovieListView.as_view(GENRE='미스터리'), name='mestery-movie-list'),
    path('cult/', EvalGenreMovieListView.as_view(GENRE='컬트'), name='cult-movie-list'),
]
