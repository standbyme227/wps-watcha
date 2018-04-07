from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


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
    #         user = authenticate(password=password,)
    #         if not user:
    #             msg = _('Unable to log in with provided credentials.')
    #             raise serializers.ValidationError(msg, code='authorization')
    #     else:
    #         msg = _('Must include "username" and "password".')
    #         raise serializers.ValidationError(msg, code='authorization')
    #     attrs['user'] = user
    #     return attrs

    def update(self, user, validated_data):
        email = validated_data.get('email', user.email)
        user.email = email
        user.save()
        return user
