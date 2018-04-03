from django.urls import path

from ..apis import (
    AuthTokenForFacebookAccessTokenView,
)

urlpatterns = [
    path('facebook-auth-token/', AuthTokenForFacebookAccessTokenView.as_view(), )
]