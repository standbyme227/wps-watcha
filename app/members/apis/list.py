from django.contrib.auth import get_user_model
from rest_framework import generics

from ..serializers import UserSerializer

User = get_user_model()

__all__ = (
    'UserListView',
)


class UserListView(generics.ListAPIView):
    queryset = User.objects.filter(is_active=True, is_staff=False, is_superuser=False)
    serializer_class = UserSerializer
