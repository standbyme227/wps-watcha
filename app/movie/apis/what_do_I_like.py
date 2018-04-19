from rest_framework import authentication, generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import UserToMovieWithUserSerializer
from ..models import Movie


class WhatNationDoILikeView(APIView):
    queryset = Movie.objects.all()
    # serializer_class =
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        # movie = user.interesting_movie_list.filter(nation=)
        # 이 방법은 user_to_movie에 접근하는 방법인가 보다.
        kr_movie = user.movie_set.all().filter(nation='KR')
        us_movie = user.movie_set.all().filter(nation='US')
        pass
        # if kr_movie:
        #     for i in kr_movie:
        #         r = i.rating
        #         r += r
        #     kr_total_rating = r
        #     kr_total = len(kr_movie)
        #     kr_avg_rating = kr_total_rating/kr_total


class HowToRateMovieView(generics.ListAPIView):
    queryset = Movie.objects.all()
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = UserToMovieWithUserSerializer

    def get_queryset(self):
        user = self.request.user
        # serializer = UserToMovieWithUserSerializer(user, data=self.request.data, partial=True)
        # serializer.is_valid(raise_exception=True)
        # return Response(serializer.data)
        movie = user.interesting_movie_list.all()
        movie_list = []
        for item in movie:
            movie_list.append(item)
        return movie_list

    # def get_queryset(self):
    #     movie_list = self.request.query_params.getlist('pk')
    #     user_to_movie = UserToMovie.objects.filter(user=self.request.user, movie__in=movie_list)
    #     return user_to_movie