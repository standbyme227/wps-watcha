from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.compat import authenticate as rest_authenticate

User = get_user_model()

__all__ = (
    'UserSerializer',
    'EmailAuthTokenSerializer',
    'AccessTokenSerializer',
)


class AccessTokenSerializer(serializers.Serializer):
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'nickname',
            'img_profile',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'date_joined',
        )


class EmailAuthTokenSerializer(serializers.Serializer):
    # username = serializers.CharField(label=_("Username"))
    email = serializers.CharField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = rest_authenticate(request=self.context.get('request'),
                                     email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
