from django.db.models import fields
from rest_framework import serializers
from .models import CustomUser,Doner,Hospital,Patient
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class AddDonerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = Doner.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            blood_type = validated_data['blood_type'],
            first_name = validated_data['first_name'],
            email = validated_data['email'],
            chronic_diseases = validated_data['chronic_diseases'],
            # address = validated_data['address'],
            roles = validated_data['roles']
        )

        return user

    class Meta:
        model = Doner
        fields = ('username','password','first_name','email','blood_type','chronic_diseases','roles'
        )

class EditDonerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):

        user = Doner.objects.create_user(
            username=validated_data['username'],
            first_name = validated_data['first_name'],
            email = validated_data['email'],
            image =  validated_data['image'],
            chronic_diseases = validated_data['chronic_diseases'],
            phone_number = validated_data['phone_number'],
            blood_type = validated_data['blood_type'],
        )

        return user

    class Meta:
        depth = 2
        model = Doner
        fields = ('username','first_name','email','chronic_diseases','image','phone_number','blood_type'
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

        user = Hospital.objects.create_user(
            first_name = validated_data['first_name'],
            username=validated_data['username'],
            password=validated_data['password'],
            website = validated_data['website'],
            email = validated_data['email'],
            roles =  validated_data['roles']
        )

        return user

    class Meta:
        model = Hospital
        fields = ( "first_name","username", "password", "website",'email','roles' )


class EditHospitalUser(serializers.ModelSerializer):

    # password = serializers.CharField(write_only=True)
    # website = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = Hospital.objects.create_user(
            first_name = validated_data['first_name'],
            username=validated_data['username'],
            website = validated_data['website'],
            image = validated_data['image'],
            email = validated_data['email'],
            phone_number = validated_data['phone_number'],
            address = validated_data['address']
        )

        return user

    class Meta:
        model = Hospital
        # Tuple of serialized model fields (see link [2])
        fields = ( 'address',"first_name","username","website",'email','image','phone_number')



class AddPatientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = Patient.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            blood_type = validated_data['blood_type'],
            first_name = validated_data['first_name'],
            email = validated_data['email'],
            roles = validated_data['roles']
        )

        return user

    class Meta:
        model = Patient
        fields = ('username','password','first_name','email','blood_type', 'roles'
        )

class EditPatientSerializer(serializers.ModelSerializer):
    def create(self, validated_data):

        user = Patient.objects.create_user(
            username=validated_data['username'],
            first_name = validated_data['first_name'],
            email = validated_data['email'],
            image =  validated_data['image'],
            reason = validated_data['reason'],
            blood_type = validated_data['blood_type'],
            phone_number = validated_data['phone_number'],
        )

        return user

    class Meta:
        depth = 2
        model = Patient
        fields = ('username','first_name','email','reason','image', 'blood_type','phone_number'
        )



        
class BloodSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
         
        user = Doner.objects.create_user(
            first_name = validated_data['first_name'],
            email = validated_data['email'],
            image =  validated_data['image'],
            address = validated_data['address'],
            blood_type = validated_data['blood_type'],
            phone_number = validated_data['phone_number'],
            
        )

        return user

    class Meta:
        model = Doner
        depth = 2
        fields = ('first_name','email','image','address','blood_type','phone_number'
        )

from django.contrib.auth.models import User

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)