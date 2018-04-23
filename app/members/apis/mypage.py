from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404

from ..serializers.user_statistics_serializer import UserStatisticsSerializer

User = get_user_model()

__all__ = (
    'HowToRateMovieView',
)


class HowToRateMovieView(generics.RetrieveAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    queryset = User.objects.all()
    serializer_class = UserStatisticsSerializer

    def get_serializer_context(self):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        return {'user': user}









# from rest_framework import authentication, generics, permissions
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
#
# from members.serializers.user_serializer import UserMinimumSerializer
# from movie.models import Movie, UserToMovie
# from movie.serializers.user_to_movie_serializer import UserToMovieRatingSerializer
# from utils.pagination import BigResultSetPagination
#
#
# class WhatNationDoILikeView(APIView):
#     queryset = Movie.objects.all()
#     # serializer_class =
#     authentication_classes = (authentication.TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#     def get(self, request):
#         user = request.user
#         # movie = user.interesting_movie_list.filter(nation=)
#         # 이 방법은 user_to_movie에 접근하는 방법인가 보다.
#         kr_movie = user.movie_set.all().filter(nation='KR')
#         us_movie = user.movie_set.all().filter(nation='US')
#         pass
#         # if kr_movie:
#         #     for i in kr_movie:
#         #         r = i.rating
#         #         r += r
#         #     kr_total_rating = r
#         #     kr_total = len(kr_movie)
#         #     kr_avg_rating = kr_total_rating/kr_total
#
#
# # 베이스는 유저로 잡고 usertomovie로 들어가 rating에 맞는 영화의 pk를 정렬하는 방법으로 한다.
#
# class HowToRateMovieView(generics.ListAPIView):
#     permission_classes = (
#         permissions.IsAuthenticated,
#     )
#     serializer_class = UserMinimumSerializer
#     pagination_class = BigResultSetPagination
#     def get_queryset(self):
#         user = self.request.user
#         movie_list = []
#         movie_1 = user.interesting_movie_list.filter(rating=4.0)
#         movie_2 = user.interesting_movie_list.filter(rating=3.0)
#
#         movie_list.append(movie_1)
#         movie_list.append(movie_2)
#
#         return movie_list
#
# # class HowToRateMovieView(generics.ListAPIView):
# #     permission_classes = (
# #         permissions.IsAuthenticated,
# #     )
# #     serializer_class = UserToMovieRatingSerializer
# #     pagination_class = BigResultSetPagination
# #     def get_queryset(self):
# #         user = self.request.user
# #         # movie_list = []
# #         # movie_1 = user.interesting_movie_list.filter(rating=4.0)
# #         # movie_2 = user.interesting_movie_list.filter(rating=3.0)
# #         #
# #         # movie_list.append(movie_1)
# #         # movie_list.append(movie_2)
# #         #
# #         # return movie_list
# #
# #
# #         movie = user.interesting_movie_list.filter(rating=4.0)
# #         # movie = user.interesting_movie_list.values('rating').annotate(count=Count('rating'))
# #         return movie
#
# # class ItemView(ListAPIView):
# #     permission_classes = (
# #         permissions.IsAuthenticated,
# #     )
# #     queryset = Items.objects.annotate(
# #                    view_count=Sum(
# #                        When(relations_item__has_viewed=True, then=1),
# #                        output_field=IntegerField(),
# #                    ),
# #                    love_count=Sum(
# #                        When(relations_item__has_loved=True, then=1),
# #                        output_field=IntegerField(),
# #                    ),
# #                )
# #     serializer_class = UserToMovieRatingSerializer