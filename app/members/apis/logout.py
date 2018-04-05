from django.contrib.auth import get_user_model
from rest_framework import status, permissions

from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()

__all__ = (
    'LogoutView',
)


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
