from rest_framework import serializers
from django.contrib.auth import get_user_model

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
                            'last_login', 'date_joined',)


class UserDetailSerializer(serializers.ModelSerializer):
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
