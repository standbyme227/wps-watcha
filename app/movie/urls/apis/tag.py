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
    path('top/korea/', TagMovieListView.as_view(TAG='국내 누적관객수 TOP 영화'), name='top-of-korea-movie-list'),
    path('million-seller/', TagMovieListView.as_view(TAG='역대 100만 관객 돌파 영화'), name='million-seller-movie-list'),
    path('top/world/', TagMovieListView.as_view(TAG='전세계 흥행 TOP 영화'), name='top-of-the-world-movie-list'),
    path('hero/', TagMovieListView.as_view(TAG='슈퍼 히어로 영화'), name='hero-movie-list'),
    path('sports/', TagMovieListView.as_view(TAG='스포츠 영화'), name='sports-movie-list'),
    path('family/', TagMovieListView.as_view(TAG='가족'), name='family-movie-list'),
]
