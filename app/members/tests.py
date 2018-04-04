from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

User = get_user_model()


class EmailAccountsTest(APITestCase):
    # def setup(self):
    #     self.test_user = User.objects.create_user('20djshin@naver.com', '네이버계정', 'testpassword')

    def test_create_user(self):
        url = reverse('members:signup')
        data = {
            'email': 'iutv@test.com',
            'nickname': 'iuiu',
            'password': 'iu123456789'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'iutv@test.com')

    def test_login_user(self):
        url = reverse('members:email-login')
        data = {
            'email': 'iutv@test.com',
            'password': 'iu123456789'
        }
        self.test_create_user()
        response = self.client.post(url, data, format='json')
        print(response.data)
        print(response.data['token'])
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['email'], data['email'])

        # 생성된 토큰 값 비교
        created_token = Token.objects.get(user_id=response.data['user']['pk'])
        self.assertEqual(created_token.key, response.data['token'])
