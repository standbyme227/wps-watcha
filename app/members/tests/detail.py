from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

User = get_user_model()


class GetUserDetailsTest(APITestCase):
    URL = reverse('members:user-detail', kwargs={'pk': 2})

    @classmethod
    def setUpTestData(cls):
        cls.test_user_1 = User.objects.create_user(
            'twice@test.com',
            '트와이스',
            'pw123456789',
        )
        cls.test_token = Token.objects.create(user=cls.test_user_1)

        cls.test_user_2 = User.objects.create_user(
            'iuiu@test.com',
            '아이유',
            'pw123456789',
        )
        cls.test_token = Token.objects.create(user=cls.test_user_2)

    def test_get_user_details(self):
        print(User.objects.all())
        print(Token.objects.all())
        print(self.test_user_2.pk)
        token = Token.objects.get(user_id=self.test_user_2.pk)
        print(f'key {token.key}')
        # # client = APIClient()
        self.client.credentials(HTTP_Authorization='token ' + token.key)
        # header = {
        #     'HTTP_Authorization': f'Token {token.key}'
        # }
        # response = self.client.get(self.URL, {}, **header, format='json')
        response = self.client.get(self.URL)
        print(response)
        print(response.data)
        # print(Token.objects.all())
