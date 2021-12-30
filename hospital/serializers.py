from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model
from .models import customUser


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    # website = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = customUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            website = validated_data['website'],
        )

        return user

    class Meta:
        model = customUser
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", "website", "image" )
