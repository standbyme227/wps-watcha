from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.compat import authenticate as rest_authenticate

User = get_user_model()

__all__ = (
    'EmailAuthTokenSerializer',
)


class EmailAuthTokenSerializer(serializers.Serializer):
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
            # The authenticate call simply returns None for is_active=False users.
            # (Assuming the default ModelBackend authentication backend.)
            if not user:
                # msg = 'This user is a member that does not exist or has left.'
                raise serializers.ValidationError('비밀번호와 이메일을 확인해주세요')
        else:
            raise serializers.ValidationError('이메일과 비밀번호 값을 넣어줘야합니다.')

        attrs['user'] = user
        return attrs
