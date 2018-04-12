import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files import File
from rest_framework import status

from utils.file import download, get_buffer_ext

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
                'email',
            ])
        }
        response = requests.get('https://graph.facebook.com/v2.12/me', params)
        if response.status_code == status.HTTP_200_OK:
            # 응답상태 코드 200 이라면
            response_dict = response.json()
            facebook_id = response_dict['id']
            url_picture = response_dict['picture']['data']['url']
            user, _ = User.objects.get_or_create(username=facebook_id, email=None)
            if not user.img_profile:
                temp_file = download(url_picture)
                ext = get_buffer_ext(temp_file)
                user.img_profile.save(f'{user.pk}.{ext}', File(temp_file))
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

# class EmailBackend:
#     def authenticate(self, request, password):
#         confirm_password = user.password
#         mypassword = password
#         if mypassword == confirm_password:
#             raise ValidationError('비밀번호가 일치하지 않습니다.')
#         return password


# def get_user(self, user_id):
#     try:
#         return User.objects.get(pk=user_id)
#     except User.DoesNotExist:
#         return None
