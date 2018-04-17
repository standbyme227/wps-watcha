from django.urls import path, include


app_name = 'eval'

urlpatterns = [
    path('genre/', include('movie.urls.apis.eval.genre')),
    path('tag/', include('movie.urls.apis.eval.tag')),
]
