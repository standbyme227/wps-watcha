from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404

from ..serializers.user_serializer import UserMyPageTopSerializer

User = get_user_model()

__all__ = (
    'MyPageTopView',
)


class MyPageTopView(generics.RetrieveAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )

    queryset = User.objects.all()
    serializer_class = UserMyPageTopSerializer

    def get_serializer_context(self):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        return {'user': user}
