# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from Utils.regex import phone_regex
from Utils.commonFunctions import id_generator
# Create your models here.


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, role, isActive, hashKey, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, role=role, isActive=isActive, hashKey=hashKey, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, role=1, **extra_fields):
        if role == 2:
            isActive = True
        else:
            isActive = False
        hashKey = id_generator(12)
        return self._create_user(username, email, password, role, isActive, hashKey=hashKey, **extra_fields)


# Primary models

class User(AbstractBaseUser):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=40)
    email = models.EmailField(
        max_length=254,
    )
    first_name = models.CharField(max_length=15, null=False, blank=False)
    middle_name = models.CharField(max_length=15, null=True, blank=True)
    last_name = models.CharField(max_length=15, null=True, blank=True)
    contact = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    isActive = models.BooleanField(default=True)
    role = models.IntegerField()  # 1 = buyer, 2 = seller, 3 = admin
    hashKey = models.CharField(max_length=12, null=False, blank=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    class Meta:
        unique_together = (('role', 'contact'), ('role', 'email'))
        db_table = 'User'

    def get_user(self, username=None, id=None, email=None):
        """
        :param username: string
        :param id: int
        :param email: string
        :return: object if found else none
        """
        if username:
            return self.get(username=username)
        if id:
            return self.get(userId=id)
        if email:
            return self.get(email=email)
        return None


class Provider(models.Model):
    companyId = models.AutoField(max_length=5, primary_key=True)
    companyAuthKey = models.CharField(max_length=50)
    companyName = models.CharField(max_length=100)
    companyContact = models.CharField(max_length=40)
    companyEmail = models.CharField(max_length=150)
    publicKey = models.CharField(max_length=50, default=None, null=True)
    companyLogo = models.CharField(max_length=100, default=None, null=True)
    companySpeciality = models.CharField(max_length=300, default=None, null=True)  # create another table
    # companyType = models.CharField(max_length=100, default="")
    companyTimingsFrom = models.TimeField(default=None, null=True)
    companyTimingsTo = models.TimeField(default=None, null=True)
    companyAddress = models.CharField(max_length=200, default=None, null=True)
    companyWebsite = models.CharField(max_length=100, default=None, null=True)
    companyArea = models.CharField(max_length=100, default=None, null=True)
    companyCity = models.CharField(max_length=100, default=None, null=True)
    companyPinCode = models.IntegerField(default=None, null=True)
    # companyMetaId = models.ForeignKey(companyMeta,on_delete=models.CASCADE)
    companyURL = models.CharField(max_length=100, default=None, null=True)
    location = models.CharField(max_length=1000, default=None, null=True)
    SMSHardStopFlag = models.BooleanField(default=False)
    EmailHardStopFlag = models.BooleanField(default=False)
    customerServiceMobile = models.CharField(max_length=30, default=None, null=True)
    customerServiceEmail = models.EmailField(max_length=255, default=None, null=True)
    isActive = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)
    countryCode = models.IntegerField(default='91')
    # slotSettingsId = models.ForeignKey(slotSettings)
    primaryColor = models.CharField(max_length=10, default="fff8e7")
    hindiMessageFlag = models.BooleanField(default=False)
    otherDetails = models.CharField(max_length=100, default=None, null=True)
    companyTimings = models.CharField(max_length=255, default=None, null=True)
    onlinePayment = models.IntegerField(default='0')

    class Meta:
        db_table = 'providerDetails'


class CompanyUser(models.Model):
    companyUserId = models.AutoField(primary_key=True)
    userId = models.OneToOneField(User, unique=True, related_name='Company_user', on_delete=models.CASCADE)
    providerId = models.ForeignKey(Provider)
    isActive = models.BooleanField(default=False)
    firstLogin = models.BooleanField(default=True)
    isAdmin = models.BooleanField(default=False)
    countryCode = models.CharField(max_length=20, default='91')
    contact = models.CharField(max_length=12, default=None, null=True)
    profilePicture = models.CharField(max_length=30, default=None, null=True)

    class Meta:
        db_table = 'CompanyUser'
