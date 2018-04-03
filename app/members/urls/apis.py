from django.urls import path


# from .. import apis
from ..apis import (
    AuthTokenForFacebookAccessTokenView,
    AuthTokenView,
    UserList,
    UserDetail,
    SignupView,
)

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
    path('auth-token/', AuthTokenView.as_view()),
    path('signup/', SignupView.as_view()),
    path('facebook-auth-token/', AuthTokenForFacebookAccessTokenView.as_view(), )
]

