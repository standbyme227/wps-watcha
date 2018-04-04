from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

__all__ = (
    'FacebookAccessTokenSerializer',
)


class FacebookAccessTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField()

    def validate(self, attrs):
        access_token = attrs.get('access_token')
        if access_token:
            # 이 안에 처리되는 부분을 backends.py 로 빼서 authenticate 안쪽으로 포함시켰다.
            user = authenticate(access_token=access_token)
            if not user:
                raise serializers.ValidationError('액세스 토큰이 올바르지 않습니다.')
        else:
            raise serializers.ValidationError('액세스 토큰이 필요합니다.')

        attrs['user'] = user
        return attrs
