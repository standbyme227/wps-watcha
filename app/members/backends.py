import requests
from django.contrib.auth import get_user_model
from rest_framework import status

from config import settings

User = get_user_model()

class APIFacebookBackend:
    CLIENT_ID = settings.FACEBOOK_APP_ID
    CLIENT_SECRET = settings.FACEBOOK_SECRET_CODE

    def authenticate(self, request, access_token):
        params = {
            'access_token': access_token,
            'fields': ','.join([
                'id',
                'name',
                'picture.width(2500)',
                'first_name',
                'last_name',
            ])
        }
        response = requests.get('https://graph.facebook.com/v2.12/me', params)
        if response.status_code == status.HTTP_200_OK:
            # 응답상태 코드 200 이라면
            response_dict = response.json()
            facebook_id = response_dict['id']
            user, _ = User.objects.get_or_create(username=facebook_id)
            return user


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
