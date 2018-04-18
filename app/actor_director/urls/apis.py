from django.urls import path

from ..apis import MovieMemberDetailView

app_name = 'movie-members'

urlpatterns = [
    path('<int:pk>/', MovieMemberDetailView.as_view(), name='movie-member-detail'),
]
