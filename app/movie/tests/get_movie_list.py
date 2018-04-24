import random

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from movie.models import Movie, UserToMovie, Genre, Tag, MovieToGenre

User = get_user_model()
print('get_movie_list.py --> start')


class GetMovieListTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        user_list = (
            ('test@gmail.com', '신종민', '1234'),
            ('django@gmail.com', '이한영', '4321'),
            ('deploy@gmail.com', '조승리', '1223344232'),
            ('airbnb@gmail.com', '박수민', 'fffe3334242'),
            ('modeling@gmail.com', '신동진', '33dd33d232')
        )
        # 유저 생성에 사용될 required 정보를 담은 list

        for user in user_list:
            user = User.objects.create_user(user[0], user[1], user[2])
            Token.objects.create(user=user)
        # list의 정보를 이용해서 user를 생성하고 토큰 부여.

        movie_list = (
            ('매트릭스', 'matrix', 120),
            ('명량', 'myungryang', 130),
            ('사랑의 모양', 'shape of water', 100),
            ('인터스텔라', 'interstella', 999),
            ('인셉션', 'inception', 888),
            ('단편', 'short', 5),
            ('장편', 'long', 200),
            ('어바웃 타임', 'about time', 120)
        )
        # 영화 생성에 필요한 정보를 담은 list

        genre_list = (
            '액션', '공포', '로맨틱코미디', '로맨스', 'SF', '드라마',
        )
        # genre 생성을 위한 list
        genre_objects_list = []
        for genre in genre_list:
            genre, _ = Genre.objects.get_or_create(genre=genre)
            # get_or_create는 tuple이 반환된다.
            genre_objects_list.append(genre)
            # print(genre)
        tag_list = (
            '전세계 흥행 TOP 영화', '국내 누적관객수 TOP 영화', '가족'
        )

        for tag in tag_list:
            tag = Tag.objects.get_or_create(tag=tag)
            # print(tag)

        a = []
        for movie in movie_list:
            a_movie = Movie.objects.create(
                title_ko=movie[0],
                title_en=movie[1],
                running_time=movie[2],
            )
            a.append(a_movie)
            # a_movie.genre.get(genre=movie[3])
            # a_movie.tag.create(genre=movie[4])
            # ManyToMany 인스턴스에 직접적으로 create는 못시킨다.
            # 연결되어있는 필드라서 당연한건데 몰라서 계속 시도해봤다.

            # print(movie)
        # list의 정보를 이용해서 영화를 생성
        b = genre_objects_list

        genre_sample_data_list = (
            (a[0], b[0]),
            (a[1], b[0]),
            (a[2], b[3]),
            (a[3], b[5]),
            (a[4], b[4]),
            (a[5], b[1]),
            (a[6], b[2]),
            (a[7], b[3]),
        )

        for genre_sample_data in genre_sample_data_list:
            MovieToGenre.objects.create(
                movie=genre_sample_data[0],
                genre=genre_sample_data[1]
            )

        eval_sample_data_list = (
            # data의 순서는
            # 보고싶어요, 봤어요, 평점, 코멘트, user, movie
            (True, False, None, '', 2, 1),
            (False, True, '4.5', '민식이형~', 1, 2),
            (False, True, '5.0', '역시 매트릭스', 1, 1),
            (False, True, '5.0', '인생영화', 1, 8),
            (False, True, '3.5', '재밌었다', 4, 3),
            (True, False, None, '', 5, 5),
            (True, False, None, '', 4, 2)
        )
        for eval_sample_data in eval_sample_data_list:
            UserToMovie.objects.create(
                user_want_movie=eval_sample_data[0],
                user_watched_movie=eval_sample_data[1],
                rating=eval_sample_data[2],
                comment=eval_sample_data[3],
                user=User.objects.get(pk=eval_sample_data[4]),
                movie=Movie.objects.get(pk=eval_sample_data[5]),

            )

    def get_user_count(self):
        return User.objects.count()

    def get_movie_count(self):
        return Movie.objects.count()

    def get_user_pk_list(self):
        return [user.pk for user in User.objects.all()]

    def get_test_user_pk(self):
        pk_list = self.get_user_pk_list()
        random.shuffle(pk_list)
        return pk_list.pop()

    def test_get_box_office_movie_list(self):
        test_user_pk = self.get_test_user_pk()
        token = Token.objects.get(user_id=test_user_pk)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('apis:movie:box-office:box-office-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        name_url = reverse('apis:movie:box-office:box-office-ranking-name-list')
        response = self.client.get(name_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        five_url = reverse('apis:movie:box-office:box-office-five-list')
        response = self.client.get(five_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_eval_movie_list(self):
        test_user_pk = self.get_test_user_pk()
        token = Token.objects.get(user_id=test_user_pk)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        rating_top_url = reverse('apis:movie:eval:rating-top')
        response = self.client.get(rating_top_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        genre_action_url = reverse('apis:movie:eval:eval-genre:action-movie-list')
        response = self.client.get(genre_action_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tag_family_url = reverse('apis:movie:eval:eval-tag:family-movie-list')
        response = self.client.get(genre_action_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_main_movie_list(self):
        test_user_pk = self.get_test_user_pk()
        token = Token.objects.get(user_id=test_user_pk)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        genre_action_url = reverse('apis:movie:genre:action-movie-list')
        response = self.client.get(genre_action_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tag_family_url = reverse('apis:movie:tag:family-movie-list')
        response = self.client.get(tag_family_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)