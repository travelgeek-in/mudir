# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework import status
import uuid
from serializers import *
import jwt
from rest_framework.renderers import JSONRenderer
from django.db import transaction
from django.contrib.auth import get_user_model, authenticate
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.compat import get_username_field, PasswordField


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


def _create_company_user(data):
    try:
        company_user = CompanyUser()
        company_user.userId_id = data['userId']
        company_user.providerId_id = data['providerId']
        company_user.isActive = False
        company_user.isAdmin = data['isAdmin']
        company_user.countryCode = data['countryCode']
        company_user.contact = data['contact']
        company_user.profilePicture = data['profilePicture']
        company_user.save()
        return company_user
    except Exception as e:
        return str(e)


@api_view(['POST'])
@permission_classes(())
def create_company_user(request):
    try:
        data = request.data
        user = create_user(data)
        data['userId'] = user.userId
        company_user = _create_company_user(data)
        if isinstance(company_user, CompanyUser):
            return Response(status=status.HTTP_200_OK)
        else:
            Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def create_user(data):
    try:
        req_data = data
        serialized = UserSerializer(data=req_data)
        if serialized.is_valid():
            get_user_model().objects.create_user(username=req_data['username'], password=req_data['password'],
                                                 contact=req_data['contact'],email=req_data['email'],
                                                 role=req_data['role'], first_name=req_data['first_name'],
                                                 middle_name=req_data['middle_name'], last_name=req_data['last_name'])
            user_object = get_user_model().objects.get(username=req_data['username'])
            return user_object
        else:
            return str(serialized._errors())
    except Exception as e:
        return str(e)


@renderer_classes((JSONRenderer,))
def get_user(request):
    token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
    token_payload = jwt.decode(token, None, None)
    return Response(token_payload)


@api_view(['POST'])
@permission_classes(())
def create_provider(request):
    try:
        with transaction.atomic():
            data = request.data

            provider_obj = Provider()
            provider_obj.companyName = data['companyName']
            provider_obj.countryCode = data['countryCode']
            provider_obj.companyContact = data['companyContact']
            provider_obj.companyEmail = data['companyEmail']
            provider_obj.companyAuthKey = uuid.uuid4()
            provider_obj.companyPinCode = data['companyPinCode']

            # provider_obj.companyLogo = data['imgURL']
            provider_obj.companySpeciality = data['companySpeciality']
            provider_obj.companyTimingsFrom = data['companyTimingsFrom']
            provider_obj.companyTimingsTo = data['companyTimingsTo']
            provider_obj.companyAddress = data['companyAddress']
            provider_obj.companyWebsite = data['companyWebsite']
            provider_obj.companyArea = data['companyArea']
            provider_obj.companyCity = data['companyCity']
            provider_obj.location = data['location']
            provider_obj.SMSHardStopFlag = data['SMSHardStopFlag']
            provider_obj.EmailHardStopFlag = data['EmailHardStopFlag']
            provider_obj.isActive = True
            provider_obj.isVerified = False
            provider_obj.onlinePayment = data['onlinePayment']

            provider_obj.save()

            data_ = dict()
            data_['providerId'] = provider_obj.companyId
            data_['username'] = data['username']
            data_['password'] = data['password']
            data_['first_name'] = data['first_name']
            data_['middle_name'] = data['middle_name']
            data_['last_name'] = data['last_name']
            data_['contact'] = data['contact']
            data_['email'] = data['email']
            data_['countryCode'] = data['countryCode']
            data_['profilePicture'] = data['profilePicture']
            data_['isAdmin'] = data['isAdmin']
            data_['role'] = 2 if data_['isAdmin'] else 1
            user = create_user(data_)
            if isinstance(user, User):
                data_['userId'] = user.userId
                data_['providerId'] = provider_obj.companyId

                # CREATE ADMIN USER
                company_user = _create_company_user(data_)

                # send confirmation email
            else:
                raise RuntimeError

        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_user(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    token_payload = jwt.decode(token, None, None)
    return Response(token_payload)


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
                        msg = _('User account is disabled.')
                        raise serializers.ValidationError(msg)

                    payload = jwt_payload_handler(user)

                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    msg = _('Unable to log in with provided credentials.')
                    raise serializers.ValidationError(msg)

            else:
                msg = _('Must include "{username_field}" and "password".')
                msg = msg.format(username_field=self.username_field)
                raise serializers.ValidationError(msg)

        else:
            msg = _('Account with this email/username does not exists')
            raise serializers.ValidationError(msg)
