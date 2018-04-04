from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from ..permissions import IsOwnerOrReadOnly
from ..serializers import UserSerializer

User = get_user_model()

__all__ = (
    'UserDetailView',
)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )
