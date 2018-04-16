from django.urls import path

from ...apis import (
    GenreMovieListView,
)

app_name = 'movie'

urlpatterns = [
    path('action/', GenreMovieListView.as_view(GENRE='액션'), name='action-movie-list'),
    path('crime/', GenreMovieListView.as_view(GENRE='범죄'), name='crime-movie-list'),
    path('drama/', GenreMovieListView.as_view(GENRE='드라마'), name='drama-movie-list'),
    path('comedy/', GenreMovieListView.as_view(GENRE='코미디'), name='comedy-movie-list'),
    path('romance/', GenreMovieListView.as_view(GENRE='로맨스/멜로'), name='romance-movie-list'),
    path('thriller/', GenreMovieListView.as_view(GENRE='스릴러'), name='thriller-movie-list'),
    path('roco/', GenreMovieListView.as_view(GENRE='로맨틱코미디'), name='roco-movie-list'),
    path('war/', GenreMovieListView.as_view(GENRE='전쟁'), name='war-movie-list'),
    path('fantasy/', GenreMovieListView.as_view(GENRE='판타지'), name='fantasy-movie-list'),
    path('sf/', GenreMovieListView.as_view(GENRE='SF'), name='sf-movie-list'),
    path('animation/', GenreMovieListView.as_view(GENRE='애니메이션'), name='animation-movie-list'),
    path('documentary/', GenreMovieListView.as_view(GENRE='다큐멘터리'), name='documentary-movie-list'),
    path('horror/', GenreMovieListView.as_view(GENRE='공포'), name='horror-movie-list'),
    path('western/', GenreMovieListView.as_view(GENRE='서부'), name='western-movie-list'),
    path('musical/', GenreMovieListView.as_view(GENRE='뮤지컬'), name='musical-movie-list'),
    path('martial-arts/', GenreMovieListView.as_view(GENRE='무협'), name='martial-arts-movie-list'),
    path('mistery/', GenreMovieListView.as_view(GENRE='미스터리'), name='mestery-movie-list'),
    path('cult/', GenreMovieListView.as_view(GENRE='컬트'), name='cult-movie-list'),
]
