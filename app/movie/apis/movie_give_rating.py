# from django.contrib.auth import get_user_model
# from rest_framework import permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from ..models import UserToMovie
# from ..serializers import UserToMovieBasicSerializer
#
# User = get_user_model()
#
# __all__ = (
#     'UserGiveRatingStar',
# )
#
#
# class UserGiveRatingStar(APIView):
#     permission_classes = (
#         permissions.IsAuthenticated,
#     )
#
#     def put(self, request, format=None):
#         token = Token.objects.get(user=request.user)
#         user = User.objects.get(auth_token=token)
#         serializer = UserSerializer(user, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#         return Response(serializer.data)