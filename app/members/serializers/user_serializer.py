from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

__all__ = (
    'UserSerializer',
    'UserEmailSerializer',
    'UserSimpleDetailSerializer',
    'UserMinimumSerializer',
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
        read_only_fields = ('pk', 'username', 'email')


class UserMinimumSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'nickname',
            'img_profile',
        )


class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'username',
        )
        # read_only_fields = ('pk', 'username',)


class UserSimpleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'nickname',
            'img_profile',
        )
