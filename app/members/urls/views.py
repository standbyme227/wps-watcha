from django.urls import path

from ..views import (
    facebook_login_backup,
    login_view,
    logout_view,
    signup_view,
)

app_name = 'members'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('facebook-login/', facebook_login_backup, name='facebook-login'),
    path('signup/', signup_view, name='signup'),
]
