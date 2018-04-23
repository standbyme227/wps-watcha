from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

User = get_user_model()
print('signup.py --> start')


class SignupTest(APITestCase):
    URL = reverse('apis:members:signup')

    # test용 DB data 초기화 메소드
    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(
            'twice@naver.com',
            '트와이스',
            'pw123456789',
        )

    def test_create_user(self):
        data = {
            'email': 'iutv@test.com',
            'nickname': 'iuiu',
            'password': 'iu123456789'
        }
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(nickname=data['nickname']).email, data['email'])
        self.assertEqual(User.objects.get(email=data['email']).nickname, data['nickname'])
        # 생성된 토큰 값 비교
        created_token = Token.objects.get(user_id=response.data['user']['pk'])
        self.assertEqual(created_token.key, response.data['token'])

    def test_create_user_with_no_password(self):
        data = {
            'email': 'iutv@test.com',
            'nickname': 'iuiu',
            'password': ''
        }
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['password']), 1)

    def test_create_user_with_no_email(self):
        data = {
            'email': '',
            'nickname': 'iuiu',
            'password': 'iu123456789'
        }
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)

    def test_create_user_with_preexisting_email(self):
        data = {
            'email': 'twice@naver.com',
            'nickname': 'iuiu',
            'password': 'iu123456789'
        }
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)

    def test_create_user_with_invalid_email(self):
        data = {
            'email': 'twice',
            'nickname': 'iuiu',
            'password': 'iu123456789'
        }
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['email']), 1)

    def test_create_user_with_no_nickname(self):
        data = {
            'email': 'iutv@test.com',
            'nickname': '',
            'password': 'iu123456789'
        }
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(len(response.data['nickname']), 1)

    # def test_create_user_with_preexisting_nickname(self):
    #     data = {
    #         'email': 'iutv@test.com',
    #         'nickname': '트와이스',
    #         'password': 'iu123456789'
    #     }
    #     user_all = User.objects.all()
    #     print(f'user_all: {user_all}')
    #     response = self.client.post(self.URL, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(User.objects.count(), 1)
    #     self.assertEqual(len(response.data['nickname']), 1)
