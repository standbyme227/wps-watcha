from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

User = get_user_model()


class EmailLoginTest(APITestCase):
    URL = reverse('apis:members:email-login')

    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(
            'twice@naver.com',
            '트와이스',
            'pw123456789',
        )

    def test_login_user(self):
        data = {
            'email': 'twice@naver.com',
            'password': 'pw123456789'
        }
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['email'], data['email'])

        # 생성된 토큰 값 비교
        self.assertEqual(Token.objects.count(), 1)
        created_token = Token.objects.get(user_id=response.data['user']['pk'])
        self.assertEqual(created_token.key, response.data['token'])

    def test_login_user_with_no_email(self):
        data = {
            'email': '',
            'password': 'pw123456789'
        }
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Token.objects.count(), 0)

    def test_login_user_with_does_not_email(self):
        data = {
            'email': 'iuiu@naver.com',
            'password': 'pw123456789'
        }
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Token.objects.count(), 0)

    def test_login_user_with_no_password(self):
        data = {
            'email': 'twice@naver.com',
            'password': ''
        }
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Token.objects.count(), 0)

    def test_login_user_with_does_not_password(self):
        data = {
            'email': 'twice@naver.com',
            'password': '0000'
        }
        response = self.client.post(self.URL, data, format='json')
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Token.objects.count(), 0)
