import random

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from movie.models import Movie

User = get_user_model()


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

        for user in user_list:
            user = User.objects.create_user(user[0], user[1], user[2])
            Token.objects.create(user=user)

        movie_list = (
            ('매트릭스', 120),
            ('인터스텔라', 999),
            ('인셉션', 888),
            ('단편', 5),
        )

        for movie in movie_list:
            movie = Movie.create_movie(movie[0], movie[1])

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

    def test_get_movie_list(self):
        test_user_pk = self.get_test_user_pk()
        token = Token.objects.get(user_id=test_user_pk)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    #
    # def test_get_user_details(self):
    #     test_user_pk = self.get_test_user_pk()
    #     token = Token.objects.get(user_id=test_user_pk)
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    #     url = reverse('apis:members:user-detail', kwargs={'pk': test_user_pk})
    #     response = self.client.get(url, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['email'], User.objects.get(pk=test_user_pk).email)
    #     self.assertEqual(response.data['nickname'], User.objects.get(pk=test_user_pk).nickname)
