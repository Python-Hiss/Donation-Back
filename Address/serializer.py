from django.db.models import fields
from rest_framework import serializers
from .models import Address, Area,City

class AddAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id','area')


class AddCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id','city')

class AddAddressSerializer(serializers.ModelSerializer):
    class Meta:

        model = Address
        fields = ('id','city','area','direction')


class viewAddressSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Address
        fields = ('id','city','area','direction')