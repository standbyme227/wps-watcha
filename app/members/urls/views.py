from sys import path
from ..views import facebook_login_backup

urlpatterns = [
    path('facebook-login/', facebook_login_backup, name='facebook-login'),
]
