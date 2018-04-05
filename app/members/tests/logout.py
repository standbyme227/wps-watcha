from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

User = get_user_model()


class LogoutTest(APITestCase):
    URL = reverse('members:logout')

    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(
            'twice@naver.com',
            '트와이스',
            'pw123456789',
        )
        cls.test_token = Token.objects.create(user=cls.test_user)

    # def test_logout_user(self):
    #     print(User.objects.all())
    #     print(Token.objects.all())
    #     token = Token.objects.first()
    #     print(f'key {token.key}')
    #     client = APIClient()
    #     client.credentials(HTTP_Authorization='Token ' + token.key)
    #     # headers = {
    #     #     'HTTP_Authorization': 'token ' + str(token)
    #     # }
    #     response = client.get(self.URL, format='json')
    #     print(response)
    #     print(response.headers)
    #     print(response.data)
