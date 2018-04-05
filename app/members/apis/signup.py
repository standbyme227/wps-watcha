from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
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
                data = {"password": ["This field may not be blank."]}
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(
                email=serializer.initial_data['email'],
                nickname=serializer.initial_data['nickname'],
                password=serializer.initial_data['password'],
            )
            token, is_create = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'user': UserSerializer(user).data,
            }
            return Response(data, status=status.HTTP_201_CREATED)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
