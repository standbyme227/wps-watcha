from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import UserSerializer

User = get_user_model()

__all__ = (
    'SignupView',
)


class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if not serializer.initial_data['password']:
                return Response('비밀번호를 입력하지 않아 ', status=status.HTTP_400_BAD_REQUEST)
            User.objects.create_user(
                email=serializer.initial_data['email'],
                nickname=serializer.initial_data['nickname'],
                password=serializer.initial_data['password'],
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class UserList(APIView):
#     def get(self, request, format=None):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class UserDetail(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get(self, request):
#         # user = self.request.user
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)
