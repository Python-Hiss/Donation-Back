from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model
from .models import customUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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
        

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['id'] = self.user.id
        data['username'] = self.user.username
        return data