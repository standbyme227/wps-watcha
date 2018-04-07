# from django.contrib.auth import get_user_model
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APITestCase
#
# User = get_user_model()
#
#
# class FacebookLoginTest(APITestCase):
#     URL = reverse('members:facebook-login')
#
#     # test용 DB data 초기화 메소드
#     @classmethod
#     def test_create_user(self):
#         data = {
#             'access_token': 'iutv@test.com',
#             'nickname': 'iuiu',
#             'password': 'iu123456789'
#         }
#         response = self.client.post(self.URL, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(User.objects.count(), 2)
#         self.assertEqual(User.objects.last().email, data['email'])
#         self.assertEqual(User.objects.last().nickname, data['nickname'])
#         # 생성된 토큰 값 비교
#         created_token = Token.objects.get(user_id=response.data['user']['pk'])
#         self.assertEqual(created_token.key, response.data['token'])
#
#
#
