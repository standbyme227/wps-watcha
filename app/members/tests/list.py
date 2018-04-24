import random

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from utils.pagination import SmallResultSetPagination

User = get_user_model()
print('list.py --> start')


class GetUserListTest(APITestCase):
    URL = reverse('apis:members:user-list')
    TEST_USER_CNT = 25

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

    def get_user_pk_list(self):
        return [user.pk for user in User.objects.all()]

    def get_test_user_pk(self):
        pk_list = self.get_user_pk_list()
        random.shuffle(pk_list)
        return pk_list.pop()

    def test_get_user_list(self):
        response = self.client.get(self.URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], User.objects.count())

        # page 체크
        if self.TEST_USER_CNT > SmallResultSetPagination.page_size:
            self.assertEqual(len(response.data['results']), SmallResultSetPagination.page_size)
            self.assertIsNotNone(response.data['next'])
        else:
            self.assertIsNone(response.data['next'])

    def get_check_user(self, url=reverse('apis:members:user-list'), pk=1):
        response = self.client.get(url, format='json')

        page_pk_list = []
        for result in response.data['results']:
            page_pk_list.append(result['pk'])

        if pk in page_pk_list:
            self.assertIn(pk, page_pk_list)
        else:
            next_url = response.data['next']
            self.get_check_user(next_url, pk=pk)

    def test_check_user_in_results(self):
        test_user_pk = self.get_test_user_pk()
        self.get_check_user(pk=test_user_pk)
