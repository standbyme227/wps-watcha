from django.urls import path

# from .. import apis
from ..apis import (
    AuthTokenForFacebookAccessTokenView,
    Logout,
    AuthTokenView,
    UserList,
    UserDetail,
    SignupView,
)

app_name = 'members'

urlpatterns = [
    path('facebook-auth-token/', AuthTokenForFacebookAccessTokenView.as_view(), name='facebook-login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
    path('auth-token/', AuthTokenView.as_view()),
    path('signup/', SignupView.as_view()),
]
