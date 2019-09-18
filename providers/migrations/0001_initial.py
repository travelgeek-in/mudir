# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-09-16 17:15
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import providers.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('companyUserId', models.AutoField(primary_key=True, serialize=False)),
                ('isActive', models.BooleanField(default=False)),
                ('firstLogin', models.BooleanField(default=True)),
                ('isAdmin', models.BooleanField(default=False)),
                ('countryCode', models.CharField(default='91', max_length=20)),
                ('contact', models.CharField(default=None, max_length=12, null=True)),
                ('profilePicture', models.CharField(default=None, max_length=30, null=True)),
            ],
            options={
                'db_table': 'CompanyUser',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('companyId', models.AutoField(max_length=5, primary_key=True, serialize=False)),
                ('companyAuthKey', models.CharField(max_length=50)),
                ('companyName', models.CharField(max_length=100)),
                ('companyContact', models.CharField(max_length=40)),
                ('companyEmail', models.CharField(max_length=150)),
                ('publicKey', models.CharField(default=None, max_length=50, null=True)),
                ('companyLogo', models.CharField(default=None, max_length=100, null=True)),
                ('companySpeciality', models.CharField(default=None, max_length=300, null=True)),
                ('companyTimingsFrom', models.TimeField(default=None, null=True)),
                ('companyTimingsTo', models.TimeField(default=None, null=True)),
                ('companyAddress', models.CharField(default=None, max_length=200, null=True)),
                ('companyWebsite', models.CharField(default=None, max_length=100, null=True)),
                ('companyArea', models.CharField(default=None, max_length=100, null=True)),
                ('companyCity', models.CharField(default=None, max_length=100, null=True)),
                ('companyPinCode', models.IntegerField(default=None, null=True)),
                ('companyURL', models.CharField(default=None, max_length=100, null=True)),
                ('location', models.CharField(default=None, max_length=1000, null=True)),
                ('SMSHardStopFlag', models.BooleanField(default=False)),
                ('EmailHardStopFlag', models.BooleanField(default=False)),
                ('customerServiceMobile', models.CharField(default=None, max_length=30, null=True)),
                ('customerServiceEmail', models.EmailField(default=None, max_length=255, null=True)),
                ('isActive', models.BooleanField(default=False)),
                ('isVerified', models.BooleanField(default=False)),
                ('countryCode', models.IntegerField(default='91')),
                ('primaryColor', models.CharField(default='fff8e7', max_length=10)),
                ('hindiMessageFlag', models.BooleanField(default=False)),
                ('otherDetails', models.CharField(default=None, max_length=100, null=True)),
                ('companyTimings', models.CharField(default=None, max_length=255, null=True)),
                ('onlinePayment', models.IntegerField(default='0')),
            ],
            options={
                'db_table': 'providerDetails',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=40, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=15)),
                ('middle_name', models.CharField(blank=True, max_length=15, null=True)),
                ('last_name', models.CharField(blank=True, max_length=15, null=True)),
                ('contact', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message=b"Contact number must be entered in the format: '+999999999", regex=b'^\\+?1?\\d{9,15}$')])),
                ('isActive', models.BooleanField(default=True)),
                ('role', models.IntegerField()),
                ('hashKey', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'User',
            },
            managers=[
                ('objects', providers.models.CustomUserManager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('role', 'email'), ('role', 'contact')]),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='providerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.Provider'),
        ),
        migrations.AddField(
            model_name='companyuser',
            name='userId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Company_user', to='providers.User'),
        ),
    ]
