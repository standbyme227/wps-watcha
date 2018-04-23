import filecmp
import random

import os
from django.contrib.auth import get_user_model
from django.core.files.storage import default_storage
from django.core.files.temp import NamedTemporaryFile
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from config import settings

User = get_user_model()


class GetUserDetailsTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user_list = (
            ('twice@test.com', '트와이스', 'pw123456789'),
            ('iuiu@test.com', '아이유', 'pw123456789'),
            ('omg@test.com', 'ohmygirl', 'abc123456789'),
        )
        # 생성할 test유저 정보를 명시해서 list에 저장시킨다
        for user in user_list:
            # user는 user_list를 돌면서 하나씩 정보를 갖는다.
            user = User.objects.create_user(user[0], user[1], user[2])
            # user는 user_list의 정보로 생성한다.
            Token.objects.create(user=user)
            # Token은 user의 정보로 생성한다.
            # 돌면서 총 3개의 유저를 생성한다.

    def get_user_count(self):
        return User.objects.count()

    def get_user_pk_list(self):
        return [user.pk for user in User.objects.all()]
        # User의 모든 객체를 돌면서 pk를 가져와서 list에 저장한다.

    def get_test_user_pk(self):
        pk_list = self.get_user_pk_list()
        # get_user_pk_list함수를 이용해서 pk_list를 저장한다.
        random.shuffle(pk_list)
        # pk_list를 random하게 섞는다
        return pk_list.pop()
        # pk_list 안에있는 객체를 하나 꺼낸다.

    def test_get_user_details(self):
        test_user_pk = self.get_test_user_pk()
        token = Token.objects.get(user_id=test_user_pk)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        # url = reverse('apis:members:user-detail', kwargs={'pk': test_user_pk})
        url = reverse('apis:members:user-detail')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], User.objects.get(pk=test_user_pk).email)
        self.assertEqual(response.data['nickname'], User.objects.get(pk=test_user_pk).nickname)

    # def test_get_user_details_with_different_pk(self):
    #     pk_list = self.get_user_pk_list()
    #     random.shuffle(pk_list)
    #     test_user_pk = pk_list.pop()
    #     different_pk = pk_list.pop()
    #     token = Token.objects.get(user_id=test_user_pk)
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    #     url = reverse('apis:members:user-detail', kwargs={'pk': different_pk})
    #     response = self.client.get(url, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    #     # self.assertEqual(len(response.data), 1)

    # def test_get_user_details_with_does_not_pk(self):
    #     test_user_pk = self.get_test_user_pk()
    #     token = Token.objects.get(user_id=test_user_pk)
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    #
    #     user_cnt = self.get_user_count()
    #     does_not_pk = user_cnt + random.randrange(1, 100)
    #     url = reverse('apis:members:user-detail', kwargs={'pk': does_not_pk})
    #
    #     response = self.client.get(url, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_user_details_with_invalid_token(self):
        temp_token = 'c60101d80b61cfd0a7f90b203475dbd08ed504fd'
        invalid_token = ''.join(random.sample(temp_token, len(temp_token)))
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + invalid_token)
        url = reverse('apis:members:user-detail')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_user_details(self):
        test_user_pk = self.get_test_user_pk()
        # get_test_user_pk라는 함수를 이용해서 test_user의 pk를 가져온다.
        token = Token.objects.get(user_id=test_user_pk)
        # token 은 Token의 object중에서 test_user의 pk에 맞는 Token을 가져와서 token에 지정한다.
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        # client의 헤더에 'Token token.key(는 token의 값)을 넣어서 인증한다.
        url = reverse('apis:members:user-detail')
        # url은 members의 user-detail이 구현된 곳으로 접근한다.
        data = {
            'nickname': 'changed_nickname',
            'first_name': 'changed_first_name',
            'last_name': 'changed_last_name'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # response의 status_code가 기대한 status의 값과 같은지 비교한다.
        self.assertEqual(response.data['nickname'], User.objects.get(pk=test_user_pk).nickname)
        # response.data의 nickname과 test_user로 생성한 user의 nickname이 같은지 검사한다.
        self.assertEqual(response.data['first_name'], User.objects.get(pk=test_user_pk).first_name)
        # response.data의 first_name과 test_user로 생성한 user의 first_name이 같은지 검사한다.
        self.assertEqual(response.data['last_name'], User.objects.get(pk=test_user_pk).last_name)
        # response.data의 last_name과 test_user로 생성한 user의 last_name이 같은지 검사한다.

    def test_patch_user_email(self):
        test_user_pk = self.get_test_user_pk()
        token = Token.objects.get(user_id=test_user_pk)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('apis:members:email-update')

        data = {
            'email': 'changed_email@test.com'
        }
        response = self.client.patch(url, data, format='json')
        # self.client는 test를 위한 browser를 명시적으로 지정해준거 같다.
        # response는 self.client로 patch 메소드를 url에다가
        # data를 json형식으로 보낸다는 뜻인거같다.

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], User.objects.get(pk=test_user_pk).email)

    def test_patch_user_img_profile(self):
        file_path = os.path.join(settings.STATIC_DIR, 'test', 'aaaaa.jpeg')
        # 파일의 경로는 os.path를 이용해서 static폴더 안쪽에 있는 test폴더의 aaaaa.jpeg
        test_user_pk = self.get_test_user_pk()
        token = Token.objects.get(user_id=test_user_pk)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('apis:members:user-img-profile', kwargs={'pk': test_user_pk})

        with open(file_path, 'rb') as f:
            response = self.client.patch(url, {
                'img_profile': f,
            })

        # file_path의 파일을 열어서 'rb'???
        # rb는 read-binary인거 같다. 뜻은 당연히 이진데이터를 읽겠다 뭐 이런....
        # 아무튼 다시 file_path의 파일을 열어서 f에 저장
        # response는 self.clientdml patch 메소드를 url에다가  'img_profile'에 f를 넣어서 보낸다.

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(pk=test_user_pk)
        # user는 test_user_pk를 pk로 가지고 있는 user로 생성
        upload_file = default_storage.open(
            # upload_file은 default_storage안에 있는 user안의 img_profile의 이름을 가져온다.
            user.img_profile.name
        )
        print(upload_file)

        with NamedTemporaryFile() as temp_file:
            temp_file.write(upload_file.read())
            # 생성한 임시파일의 경로 (temp_file.name)와
            # 테스트용 정적파일의 경로 (file_path)를 이용해서
            # 같은 파일인지 비교
            print('file_path:', file_path)
            print('temp_file.name:', temp_file.name)
            temp_file.seek(0)
            self.assertTrue(filecmp.cmp(file_path, temp_file.name))
