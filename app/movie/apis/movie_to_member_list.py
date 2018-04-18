# from rest_framework import permissions, status, generics
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from utils.pagination import StandardResultSetPagination
# from ..serializers.movie_to_member_serializer import MovieToMemberSerializer
# from ..models import UserToMovie
#
#
# __all__ = (
#     'MovieMemberListView',
# )
#
#
# class MovieMemberListView(generics.ListAPIView):
#     permission_classes = (
#         permissions.IsAuthenticated,
#     )
#
#     serializer_class = MovieToMemberSerializer
#     pagination_class = StandardResultSetPagination
#
#     def get_queryset(self):
#         member_pk = self.request.query_params.getlist('pk')
#         user_to_movie = UserToMovie.objects.filter(user=self.request.user, movie__in=movie_list)
#         return user_to_movie
