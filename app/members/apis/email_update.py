from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers.authtoken_serializer import TokenSerializer
from ..permissions import IsAdminOrIsSelf

User = get_user_model()

__all__ = (
    'UserEmailUpdateView',
)


class UserEmailUpdateView(APIView):
    permission_classes = (
        IsAdminOrIsSelf,
    )

    def patch(self, request, pk):
        user = User.objects.get(id=pk)
        self.check_object_permissions(self.request, user)
        serializer = TokenSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
