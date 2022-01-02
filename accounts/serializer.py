from django.db.models import fields
from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class AddDonaterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            blood_type = validated_data['blood_type'],
            first_name = validated_data['first_name'],
            email = validated_data['email'],
            roles = validated_data['roles']
        )

        return user

    class Meta:
        model = CustomUser
        fields = ('username','password','first_name','email','blood_type','roles'
        )

class EditDonaterSerializer(serializers.ModelSerializer):
     def create(self, validated_data):

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            date_of_birth=validated_data['date_of_birth'],
            blood_type = validated_data['blood_type'],
            chronic_diseases = validated_data['chronic_diseases'],
            date = validated_data['date'],
            phone_number = validated_data['phone_number'],
            first_name = validated_data['first_name'],
            email = validated_data['email'],
            location = validated_data['location'],
            image = validated_data['image'],
            
        )

        return user
     class Meta:
        model = CustomUser
        fields = ('username','first_name','email','date_of_birth','image','location','phone_number'
        ,'date','chronic_diseases','blood_type','date'
        )

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        data['id'] = self.user.id
        data['username'] = self.user.username
        data['Role'] = self.user.roles

        return data



## hospital serializer

class AddHospitalUser(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    # website = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = CustomUser.objects.create_user(
            first_name = validated_data['first_name'],
            username=validated_data['username'],
            password=validated_data['password'],
            website = validated_data['website'],
            email = validated_data['email'],
            roles =  validated_data['roles']
        )

        return user

    class Meta:
        model = CustomUser
        # Tuple of serialized model fields (see link [2])
        fields = ( "first_name","username", "password", "website",'email','roles' )


class EditHospitalUser(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    # website = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = CustomUser.objects.create_user(
            first_name = validated_data['first_name'],
            username=validated_data['username'],
            password=validated_data['password'],
            website = validated_data['website'],
            image = validated_data['image'],
            email = validated_data['email'],
        )

        return user

    class Meta:
        model = CustomUser
        # Tuple of serialized model fields (see link [2])
        fields = ( "first_name","username", "password", "website",'email','image' )