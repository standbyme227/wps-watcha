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
    WantMovieListView,
)

app_name = 'members'

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('facebook-auth-token/', AuthTokenForFacebookAccessTokenView.as_view(), name='facebook-login'),
    path('email-auth-token/', AuthTokenForEmailView.as_view(), name='email-login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/img-profile/', UserImageUpdateView.as_view(), name='user-img-profile'),
    path('<int:pk>/email/', UserEmailUpdateView.as_view(), name='email-update'),
    path('<int:pk>/wantmovie/', WantMovieListView.as_view(), name='want-movie'),
]
