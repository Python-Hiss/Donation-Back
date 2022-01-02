from django.db.models import fields
from rest_framework import serializers
from .models import UserAccount
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class AddSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserAccount.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            age=validated_data['age'],
            # blood_type = validated_data['blood_type'],
            # chronic_diseases = validated_data['chronic_diseases'],
            # data = validated_data['data'],
            # phone_number = validated_data['phone_number'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            # location = validated_data['location'],
            # donate = validated_data['donate'],
            image = validated_data['image']
        )

        return user

    class Meta:
        model = UserAccount
        fields = ('username','password','first_name','last_name','email','age','image'
        )
from django.contrib.auth.models import Group
class EditSerializer(serializers.ModelSerializer):
     def create(self, validated_data):

        user = UserAccount.objects.create_user(
            username=validated_data['username'],
            age=validated_data['age'],
            blood_type = validated_data['blood_type'],
            chronic_diseases = validated_data['chronic_diseases'],
            date = validated_data['date'],
            phone_number = validated_data['phone_number'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            location = validated_data['location'],
            donate = validated_data['donate'],
            image = validated_data['image']
        )

        return user
     class Meta:
        model = UserAccount
        fields = ('username','first_name','last_name','email','age','image','donate','location','phone_number'
        ,'date','chronic_diseases','blood_type'
        )

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        data['id'] = self.user.id
        data['username'] = self.user.username
        data['group'] = bool(self.user.first_name)

        return data

