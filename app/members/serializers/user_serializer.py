from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

__all__ = (
    'UserSerializer',
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'username',
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
        read_only_fields = ('pk', 'username', 'is_active', 'is_staff', 'is_superuser',
                            'last_login', 'date_joined', 'email')


class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
        )

        def validate(self, attrs):
            password = attrs.get('password')
            if password:
                user = authenticate(password=password)
                if not user:
                    raise serializers.ValidationError('비밀번호가 틀렸습니다.')
            else:
                raise serializers.ValidationError('권한이 존재하지 않습니다.')
            attrs['user'] = user
            return attrs
