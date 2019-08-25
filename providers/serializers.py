from rest_framework import serializers
from models import *


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ProviderMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('companyName', 'companyContact', 'companyEmail', 'countryCode', 'companyCity', 'companyPinCode')


# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'middle_name', 'last_name', 'email', 'contact', 'password', 'role')
#
#
# class UserSerializerResponse(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'middle_name', 'last_name', 'email', 'contact', 'role')
