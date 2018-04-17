from django.urls import path, include

from ...apis import (
    MovieBoxofficeRankingNameListView,
    MovieBoxofficeRankingFiveListView,
    MovieBoxofficeRankingListView,
)

app_name = 'box-office'

urlpatterns = [
    path('name-list/', MovieBoxofficeRankingNameListView.as_view(), name='box-office-ranking-name-list'),
    path('five-list/', MovieBoxofficeRankingFiveListView.as_view(), name='box-office-ranking-name-list'),
    path('', MovieBoxofficeRankingListView.as_view(), name='box-office-ranking-name-list'),

]
