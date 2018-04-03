from django.urls import path

from ..apis import (
    AuthTokenForFacebookAccessTokenView,
    Logout,
)

app_name = 'members'

urlpatterns = [
    path('facebook-auth-token/', AuthTokenForFacebookAccessTokenView.as_view(), name='facebook-login'),
    path('logout/', Logout.as_view(), name='logout'),
    # path('list/')
]