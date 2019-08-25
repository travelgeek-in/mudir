# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from providers.models import Provider, CompanyUser

# Create your models here.


class Categories(models.Model):

    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'Categories'


class Amenity(models.Model):

    amenityId = models.AutoField(primary_key=True)
    transport = models.BooleanField(default=False)
    meals = models.BooleanField(default=True)
    hotels = models.BooleanField(default=True)
    sightSeeing = models.BooleanField(default=True)
    inTransitMeals = models.BooleanField(default=False)
    isFlight = models.BooleanField(default=False)
    isTrain = models.BooleanField(default=False)

    class Meta:
        db_table = 'Amenity'


class Trip(models.Model):

    tripId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    shortDescription = models.CharField(max_length=500)
    longDescription = models.CharField(max_length=100)
    category = models.ForeignKey(Categories)
    createdDate = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=False)
    amount1 = models.IntegerField()
    amount2 = models.IntegerField()
    onDiscount = models.BooleanField(default=False)
    providerId = models.ForeignKey(Provider)
    createdBy = models.ForeignKey(CompanyUser)

    days = models.IntegerField()
    departureDate = models.DateTimeField()
    arrivalDate = models.DateTimeField()
    departureCities = models.CharField(max_length=255)
    arrivalCities = models.CharField(max_length=255)

    itineraryId = models.CharField(max_length=255)
    amenityId = models.ForeignKey(Amenity)
    isInternational = models.BooleanField(default=False)

    cities = models.CharField(max_length=500)

    class Meta:
        db_table = 'Trip'


class ProviderCategory(models.Model):
    providerCategoryId = models.AutoField(primary_key=True)
    categoryId = models.ForeignKey(Categories)
    providerId = models.ForeignKey(Provider)

    class Meta:
        db_table = 'ProviderCategory'
