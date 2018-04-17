from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, authentication, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from ..permissions import IsAdminOrIsSelf
from ..serializers import UserSerializer

User = get_user_model()

__all__ = (
    'UserDetailView',
)


class UserDetailView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAdminOrIsSelf,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        token = Token.objects.get(user=request.user)
        user = User.objects.get(auth_token=token)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        token = Token.objects.get(user=request.user)
        user = User.objects.get(auth_token=token)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, format=None):
        token = Token.objects.get(user=request.user)
        user = User.objects.get(auth_token=token)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class UserDetailUpdateView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     permission_classes = (
#         IsAdminOrIsSelf,
#     )
#
#     # def get(self, request, *args, **kwargs):
#     #     token = Token.objects.get(user=request.user)
#     #     user = User.objects.get(auth_token=token)
#     #     serializer = self.get_serializer(user, data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     return Response(serializer.data)
#
#     def update(self, request, *args, **kwargs):
#         user_profile = self.get_object()
#         serializer = self.get_serializer(user_profile, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)
