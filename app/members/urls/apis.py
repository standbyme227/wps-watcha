from django.urls import path

from ..apis import (
    UserListView,
    UserDetailView,
    SignupView,
    AuthTokenForFacebookAccessTokenView,
    AuthTokenForEmailView,
    LogoutView,
    UserImageUpdateView,
    UserEmailUpdateView,
    WantWatchedMovieListView,
    HowToRateMovieView,
    MyPageTopView,
    SearchUserListView,
    CommentedMovieListView,
)

app_name = 'members'

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('detail/', UserDetailView.as_view(), name='user-detail'),
    path('img-profile/<int:pk>/', UserImageUpdateView.as_view(), name='user-img-profile'),
    path('email/', UserEmailUpdateView.as_view(), name='email-update'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('facebook-auth-token/', AuthTokenForFacebookAccessTokenView.as_view(), name='facebook-login'),
    path('email-auth-token/', AuthTokenForEmailView.as_view(), name='email-login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('<int:pk>/want-movie/', WantWatchedMovieListView.as_view(want_movie=True), name='want-movie'),
    path('<int:pk>/watched-movie/', WantWatchedMovieListView.as_view(watched_movie=True), name='watched-movie'),
    path('commented-movie/', CommentedMovieListView.as_view(), name='commented-movie'),

    path('rating/', HowToRateMovieView.as_view(), name='user-rating'),
    # path('')

    path('<int:pk>/mypage-top/', MyPageTopView.as_view(), name='mypage-top'),
    path('search/', SearchUserListView.as_view(), name='user-search'),

]
