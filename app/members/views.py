from django.conf import settings
from django.shortcuts import render

# Create your views here.

def facebook_login(request):
    client_id = settings.FACEBOOK_APP_ID,
    redirect_uri = 'http://localhost:8000/facebook-login/'
    client_secret = settings.FACEBOOK_SECRET_CODE
    code = request.GET['code']

    url = 'https://graph.facebook.com/v2.12/oauth/access_token'
