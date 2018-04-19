from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import generics, permissions

from ..serializers import UserSerializer
from utils.pagination import StandardResultSetPagination

User = get_user_model()

__all__ = (
    'SearchUserListView',
)


class SearchUserListView(generics.ListAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultSetPagination

    # SearchFilter 를 사용하면 search 기능을 쉽게 구현 할 수 있음.
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('nickname', 'email')

    def get_queryset(self):
        try:
            if self.request.query_params['user']:
                val = self.request.query_params['user']
                return User.objects.filter(Q(nickname__contains=val) | Q(email__contains=val))
            return User.objects.none()
        except:
            return User.objects.none()
