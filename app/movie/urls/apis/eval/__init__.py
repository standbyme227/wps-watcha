from django.urls import path, include

from movie.apis import EvalWatchaRatingTopMovieListView

app_name = 'eval'

urlpatterns = [
    path('genre/', include('movie.urls.apis.eval.genre')),
    path('tag/', include('movie.urls.apis.eval.tag')),
    path('rating-top/', EvalWatchaRatingTopMovieListView.as_view(), name='rating-top'),
]
