from django.db.models import fields
from rest_framework import serializers
from .models import BloodType

class AddBloodSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodType
        fields = ('id','blood_type','description')
