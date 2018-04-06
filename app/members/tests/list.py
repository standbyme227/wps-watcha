from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

User = get_user_model()


class GetUserListTest(APITestCase):
    URL = reverse('members:user-list')

    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(
            'twice@naver.com',
            '트와이스',
            'pw123456789',
        )

    def test_get_user_list(self):
        response = self.client.get(self.URL, {}, format='json')
        self.assertEqual(len(response.data), User.objects.count())
        self.assertEqual(response.data[0]['email'], self.test_user.email)
        self.assertEqual(response.data[0]['nickname'], self.test_user.nickname)
