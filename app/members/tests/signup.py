from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class SignupTest(APITestCase):
    URL = reverse('members:signup')

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
        self.assertEqual(User.objects.last().email, data['email'])

    def test_create_user_with_no_password(self):
        data = {
            'email': 'iutv@test.com',
            'nickname': 'iuiu',
            'password': ''
        }
        response = self.client.post(self.URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)
        print(response.data)
