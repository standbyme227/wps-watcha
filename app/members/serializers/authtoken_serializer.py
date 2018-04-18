from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

__all__ = (
    'TokenSerializer',
)


class TokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    # def validate(self, attrs):
    #     password = attrs.get('password')
    #     if password:
    #         user = rest_authenticate(password=password)
    #         if not user:
    #             raise serializers.ValidationError('비밀번호가 일치하지 않습니다.')
    #     else:
    #         raise serializers.ValidationError('비밀번호 값을 넣어줘야합니다.')
    #     attrs['user'] = user
    #     return attrs

    def update(self, user, validated_data):
        email = validated_data.get('email', user.email)
        password = validated_data.get('password', user.password)
        if not User.objects.filter(email=email):
            user.email = email
            user.save()
        else:
            raise serializers.ValidationError('중복되는 이메일 값입니다.')
        return user
