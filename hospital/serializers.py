from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import Account # If used custom user model
from .models import customUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    # website = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = customUser.objects.create_user(
            name = validated_data['name'],
            username=validated_data['username'],
            password=validated_data['password'],
            website = validated_data['website'],
            image = validated_data['image'],
            group = validated_data['group'],
            email = validated_data['email'],
        )

        return user

    class Meta:
        model = customUser
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "name","username", "password", "website", "image",'email' )
        
