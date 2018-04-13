from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response

from ..permissions import IsAdminOrIsSelf
from ..serializers import UserDetailSerializer

User = get_user_model()

__all__ = (
    'UserDetailView',
)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    permission_classes = (
        IsAdminOrIsSelf,
    )

    # def get(self, request, *args, **kwargs):
    #     token = Token.objects.get(user=request.user)
    #     user_profile = self.get_object(token=token)
    #     queryset = User.objects.filter(user)
    #     serializer_class = UserDetailSerializer
    #
    #     permission_classes = (
    #         IsAdminOrIsSelf,
    #     )


    def update(self, request, *args, **kwargs):
        user_profile = self.get_object()
        serializer = self.get_serializer(user_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

