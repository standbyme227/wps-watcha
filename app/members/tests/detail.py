import random
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

User = get_user_model()


class GetUserDetailsTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user_list = (
            ('twice@test.com', '트와이스', 'pw123456789'),
            ('iuiu@test.com', '아이유', 'pw123456789'),
            ('omg@test.com', 'ohmygirl', 'abc123456789'),
        )
        for user in user_list:
            user = User.objects.create_user(user[0], user[1], user[2])
            Token.objects.create(user=user)

    def get_user_count(self):
        return User.objects.count()

    def get_user_pk_list(self):
        return [user.pk for user in User.objects.all()]

    def get_test_user_pk(self):
        pk_list = self.get_user_pk_list()
        random.shuffle(pk_list)
        return pk_list.pop()

    def test_get_user_details(self):
        test_user_pk = self.get_test_user_pk()
        token = Token.objects.get(user_id=test_user_pk)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('members:user-detail', kwargs={'pk': test_user_pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], User.objects.get(pk=test_user_pk).email)
        self.assertEqual(response.data['nickname'], User.objects.get(pk=test_user_pk).nickname)

    def test_get_user_details_with_different_pk(self):
        pk_list = self.get_user_pk_list()
        random.shuffle(pk_list)
        test_user_pk = pk_list.pop()
        different_pk = pk_list.pop()
        token = Token.objects.get(user_id=test_user_pk)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('members:user-detail', kwargs={'pk': different_pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # self.assertEqual(len(response.data), 1)

    def test_get_user_details_with_does_not_pk(self):
        test_user_pk = self.get_test_user_pk()
        token = Token.objects.get(user_id=test_user_pk)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        user_cnt = self.get_user_count()
        does_not_pk = user_cnt + random.randrange(1, 100)
        url = reverse('members:user-detail', kwargs={'pk': does_not_pk})

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_user_details_with_invalid_token(self):
        test_user_pk = self.get_test_user_pk()
        temp_token = 'c60101d80b61cfd0a7f90b203475dbd08ed504fd'
        invalid_token = ''.join(random.sample(temp_token, len(temp_token)))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + invalid_token)
        url = reverse('members:user-detail', kwargs={'pk': test_user_pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
