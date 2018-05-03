from django.urls import path
# django urls안에 있는 path를 이용해야한다.
from ..apis import MovieMemberDetailView
# url을 연결한 view는 apis의 MovieMemberDetail이다.

app_name = 'movie-members'
# app_name을 지정함으로써 얻을 수 있는 이점은 무엇일까?? 일단 reverse할때 필요한걸로 알고 있다.
urlpatterns = [
    path('<int:pk>/', MovieMemberDetailView.as_view(), name='movie-member-detail'),
]
