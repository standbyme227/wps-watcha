import random

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from movie.models import Movie, UserToMovie

User = get_user_model()
print('user_checked_movie_create.py --> start')


class UserCheckedMovieCreate(APITestCase):
    URL = reverse('apis:movie:user-checked-movie-create')

    @classmethod
    def setUpTestData(cls):
        # (주의)setUpTestData 함수의 내용 수정 시 test 결과가 다르게 나올 수 있습니다.

        # 영화 샘플 데이터 저장
        movie_list = (
            ('빅', 'Big,1988'),
            ('몽상가들', 'TheDreamers,2003'),
            ('그레이트 뷰티', 'TheGreatBeauty,2013'),
        )
        for movie in movie_list:
            Movie.objects.create(
                title_ko=movie[0],
                title_en=movie[1],
            )

        # User 및 Token 샘플 데이터 저장
        user_list = (
            ('twice@test.com', '트와이스', 'pw123456789'),
            ('iuiu@test.com', '아이유', 'pw123456789'),
            ('omg@test.com', 'ohmygirl', 'abc123456789'),
        )
        for user in user_list:
            user = User.objects.create_user(user[0], user[1], user[2])
            Token.objects.create(user=user)

        # 평가 정보 샘플 데이터 저장
        eval_data_list = (
            (True, False, None, '', 1, 1),
            (True, False, '3.5', 'great movie~', 1, 2),
            # (False, True, '2.0', 'not bad', 1, 3),
            (False, True, '4.5', '최고의 영화입니다.', 2, 1),
            (True, False, None, '이 영화 보고싶어요', 2, 2),
            (False, True, None, 'text..', 2, 3),
            (True, False, '1.0', 'Never see this movie.', 3, 1),
            (True, False, None, 'text..', 3, 2),
            (False, True, None, '', 3, 3),
        )
        for eval_data in eval_data_list:
            UserToMovie.objects.create(
                user_want_movie=eval_data[0],
                user_watched_movie=eval_data[1],
                rating=eval_data[2],
                comment=eval_data[3],
                user=User.objects.get(pk=eval_data[4]),
                movie=Movie.objects.get(pk=eval_data[5]),
            )

    def test_get_user_checked_movie_create(self):
        test_user_pk = 1
        token = Token.objects.get(user_id=test_user_pk)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        data = {
            "user_want_movie": False,
            "user_watched_movie": True,
            "rating": "3.0",
            "comment": "good movie~",
            "movie": 3
        }
        response = self.client.post(self.URL, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user'], test_user_pk)
        self.assertEqual(response.data['movie'], data['movie'])

    def test_get_user_checked_movie_create_with_existing_data(self):
        test_user_pk = 2
        token = Token.objects.get(user_id=test_user_pk)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        data = {
            "user_want_movie": False,
            "user_watched_movie": True,
            "rating": "3.0",
            "comment": "good movie~",
            "movie": 3
        }
        response = self.client.post(self.URL, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['non_field_errors'][0],
            'The fields user, movie must make a unique set.'
        )

    def test_get_user_checked_movie_create_with_invaild_token(self):
        temp_token = 'c60101d80b61cfd0a7f90b203475dbd08ed504fd'
        invalid_token = ''.join(random.sample(temp_token, len(temp_token)))
        token_queryset = Token.objects.filter(key=invalid_token)
        data = {
            "user_want_movie": False,
            "user_watched_movie": True,
            "rating": "3.0",
            "comment": "good movie~",
            "movie": 3
        }
        if not token_queryset:
            self.client.credentials(HTTP_AUTHORIZATION='Token ' + invalid_token)
            response = self.client.get(self.URL, data=data, format='json')
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
