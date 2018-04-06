from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
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

    def test_logout_user(self):
        print(User.objects.all())
        print(Token.objects.all())
        token = Token.objects.first()
        print(f'key: {token.key}')
        # client = APIClient()
        self.client.credentials(HTTP_Authorization='Token ' + token.key)
        # header = {
        #     'HTTP_Authorization': f'Token {token.key}'
        # }
        # response = self.client.get(self.URL, {}, **header, format='json')
        response = self.client.get(self.URL)
        print(response)
        print(response.data)
        print(Token.objects.all())

        # self.client.login(email='twice@naver.com', password='pw123456789')
        # print(Token.objects.all())
        # response = self.client.get('/admin/login/')
        # print(response)
        # print(response.content)
