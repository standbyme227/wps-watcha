from django.urls import path

from ..apis import (
    UserListView,
    UserDetailView,
    SignupView,
    AuthTokenForFacebookAccessTokenView,
    AuthTokenForEmailView,
    LogoutView,
    UserImageUpdateView,
)

app_name = 'members'

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('facebook-auth-token/', AuthTokenForFacebookAccessTokenView.as_view(), name='facebook-login'),
    path('email-auth-token/', AuthTokenForEmailView.as_view(), name='email-login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('img-profile/<int:pk>/', UserImageUpdateView.as_view(), name='user-img-profile'),
]
