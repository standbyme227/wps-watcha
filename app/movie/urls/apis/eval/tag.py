from django.urls import path

from ....apis import (
    EvalTagMovieListView,
)

app_name = 'eval-tag'

urlpatterns = [
    path('top/korea/', EvalTagMovieListView.as_view(TAG='국내 누적관객수 TOP 영화'), name='top-of-korea-movie-list'),
    path('million-seller/', EvalTagMovieListView.as_view(TAG='역대 100만 관객 돌파 영화'), name='million-seller-movie-list'),
    path('top/world/', EvalTagMovieListView.as_view(TAG='전세계 흥행 TOP 영화'), name='top-of-the-world-movie-list'),
    path('hero/', EvalTagMovieListView.as_view(TAG='슈퍼 히어로 영화'), name='hero-movie-list'),
    path('sports/', EvalTagMovieListView.as_view(TAG='스포츠 영화'), name='sports-movie-list'),
    path('family/', EvalTagMovieListView.as_view(TAG='가족'), name='family-movie-list'),
]
