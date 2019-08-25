# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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
    userId = models.OneToOneField(User, unique=True, related_name='Company_user')
    providerId = models.ForeignKey(Provider)
    isActive = models.BooleanField(default=False)
    firstLogin = models.BooleanField(default=True)
    isAdmin = models.BooleanField(default=False)
    countryCode = models.CharField(max_length=20, default='91')
    contact = models.CharField(max_length=12, default=None, null=True)
    profilePicture = models.CharField(max_length=30, default=None, null=True)

    class Meta:
        db_table = 'CompanyUser'
