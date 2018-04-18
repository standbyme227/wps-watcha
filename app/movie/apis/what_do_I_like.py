from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

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
        # if kr_movie:
        #     for i in kr_movie:
        #         r = i.rating
        #         r += r
        #     kr_total_rating = r
        #     kr_total = len(kr_movie)
        #     kr_avg_rating = kr_total_rating/kr_total


