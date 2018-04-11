from django.urls import path

from ..apis import (
    MovieListView
)

app_name = 'movie'

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
]
