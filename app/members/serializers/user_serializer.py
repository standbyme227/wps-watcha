from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

__all__ = (
    'UserSerializer',
    'UserDetailSerializer',
    'UserEmailSerializer',
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
        )
        read_only_fields = ('pk', 'username',)


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
        )
        read_only_fields = ('pk', 'username', 'email',)


class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'username',
        )
        read_only_fields = ('pk', 'username',)