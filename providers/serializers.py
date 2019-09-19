from rest_framework import serializers
from models import *
from django.contrib.auth import authenticate
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.compat import PasswordField


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class CustomJWTSerializer(JSONWebTokenSerializer):
    username_field = 'username_or_email'

    def __init__(self, *args, **kwargs):
        """
        Dynamically add the USERNAME_FIELD to self.fields.
        """
        super(JSONWebTokenSerializer, self).__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields['password'] = PasswordField(write_only=True)

    def validate(self, attrs):

        password = attrs.get("password")
        user_obj = User.objects.filter(email=attrs.get("username_or_email")).first() or User.objects.filter(
            username=attrs.get("username_or_email")).first()
        if user_obj is not None:
            credentials = {
                'username': user_obj.username,
                'password': password
            }
            if all(credentials.values()):
                user = authenticate(**credentials)
                if user:
                    if not user.is_active:
                        msg = 'User account is disabled.'
                        raise serializers.ValidationError(msg)

                    payload = jwt_payload_handler(user)

                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    msg = 'Unable to log in with provided credentials.'
                    raise serializers.ValidationError(msg)

            else:
                msg = 'Must include "{username_field}" and "password".'
                msg = msg.format(username_field=self.username_field)
                raise serializers.ValidationError(msg)

        else:
            msg = 'Account with this email/username does not exists'
            raise serializers.ValidationError(msg)


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ProviderMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('companyName', 'companyContact', 'companyEmail', 'countryCode', 'companyCity', 'companyPinCode')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'middle_name', 'last_name', 'email', 'contact', 'password', 'role')


class UserSerializerResponse(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'middle_name', 'last_name', 'email', 'contact', 'role')
