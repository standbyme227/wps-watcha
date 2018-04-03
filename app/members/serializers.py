from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.compat import authenticate


User = get_user_model()

__all__ = (
    'UserSerializer',
    'EmailAuthTokenSerializer',
)


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
            user = authenticate(request=self.context.get('request'),
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
