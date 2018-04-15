
from rest_framework import generics, authentication
from rest_framework.views import APIView

from ..permissions import IsAdminOrReadOnly
from utils.pagination import MovieListDefaultPagination, BoxOfficeRankingPagination, BoxOfficeRankingFivePagination
from ..serializers import MovieListSerializer
from ..models import Movie


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    pagination_class = MovieListDefaultPagination



class MovieBoxofficeRankingView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = BoxOfficeRankingPagination

    # def get(self, request, format=None):
    #     movie = Movie.objects.filter()
    #     user = User.objects.get(auth_token=token)
    #     serializer = UserSerializer(user, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     return Response(serializer.data)