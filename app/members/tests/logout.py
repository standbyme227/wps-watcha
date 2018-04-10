import random

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

User = get_user_model()


class LogoutTest(APITestCase):
    URL = reverse('apis:members:logout')
    TEST_USER_CNT = 4

    @classmethod
    def setUpTestData(cls):
        user_data = ['test', '닉네임', 'abc123456789']
        for index in range(1, cls.TEST_USER_CNT + 1):
            user = User.objects.create_user(
                user_data[0] + str(index) + '@test.com',
                user_data[1] + str(index),
                user_data[2]
            )
            Token.objects.create(user=user)

    def test_logout_user(self):
        token = Token.objects.first()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(self.URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Token.objects.count(), self.TEST_USER_CNT - 1)

    def test_logout_user_invalid_token(self):
        sample_token = 'c60101d80b61cfd0a7f90b203475dbd08ed504fd'
        invalid_token = ''.join(random.sample(sample_token, len(sample_token)))

        for token in Token.objects.all():
            if token.key == invalid_token:
                invalid_token = ''.join(random.sample(token.key, len(sample_token)))

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + invalid_token)
        response = self.client.get(self.URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

