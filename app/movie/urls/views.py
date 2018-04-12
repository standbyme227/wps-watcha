from django.urls import path

from ..views import (
    movie_search_from_naver,
    movie_list,
    movie_add_from_naver,
    update_or_create_from_crawler
)

app_name = 'movie'

urlpatterns = [
    path('', movie_list, name='movie-list'),
    path('search/naver', movie_search_from_naver, name='movie-search-from-naver'),
    path('add/naver', movie_add_from_naver, name='movie-add-from-naver'),
    path('crawling/', update_or_create_from_crawler, name='movie-crawler'),
]
