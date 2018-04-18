from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..permissions import IsAdminOrIsSelf
from ..serializers import UserSerializer

User = get_user_model()

__all__ = (
    'UserImageUpdateView',
)


class UserImageUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    permission_classes = (
        IsAdminOrIsSelf,
    )

    def image(self, request, *args, **kwargs):
        if 'upload' in request.data:
            user_profile = self.get_object()
            user_profile.image.delete()
            upload = request.data['upload']
            user_profile.image.save(upload.name, upload)

            return Response(status=status.HTTP_201_CREATED, headers={'Location': user_profile.image.url})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# class UserImageUpdateView(APIView):
#     permission_classes = (IsAdminOrIsSelf,)
#     authentication_classes = (authentication.TokenAuthentication,)
#
#     def patch(self, request, *args, **kwargs):
#         if 'upload' in request.data:
#             token = Token.objects.get(user=request.user)
#             user = User.objects.get(auth_token=token)
#             user.img_profile.delete()
#             upload = request.data['upload']
#             user.img_profile.save(upload.name, upload)
#             return Response(status=status.HTTP_201_CREATED, headers={'Location': user.img_profile.url})
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
