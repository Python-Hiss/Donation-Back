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
            image =  validated_data['image'],
            chronic_diseases = validated_data['chronic_diseases'],
            address = validated_data['address'],
            roles = validated_data['roles']
        )

        return user

    class Meta:
        model = Doner
        fields = ('username','password','first_name','email','blood_type','address','chronic_diseases','image','roles'
        )

class EditDonerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):

        user = Doner.objects.create_user(
            username=validated_data['username'],
            first_name = validated_data['first_name'],
            email = validated_data['email'],
            image =  validated_data['image'],
            chronic_diseases = validated_data['chronic_diseases'],
            
        )

        return user

    class Meta:
        model = Doner
        fields = ('username','first_name','email','chronic_diseases','image'
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

    password = serializers.CharField(write_only=True)
    # website = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = Hospital.objects.create_user(
            first_name = validated_data['first_name'],
            username=validated_data['username'],
            website = validated_data['website'],
            image = validated_data['image'],
            email = validated_data['email'],
        )

        return user

    class Meta:
        model = Hospital
        # Tuple of serialized model fields (see link [2])
        fields = ( "first_name","username","website",'email','image' )



class AddPatientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = Patient.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            blood_type = validated_data['blood_type'],
            first_name = validated_data['first_name'],
            email = validated_data['email'],
            image =  validated_data['image'],
            reason = validated_data['reason'],
            address = validated_data['address'],
            roles = validated_data['roles']
        )

        return user

    class Meta:
        model = Patient
        fields = ('username','password','first_name','email','blood_type', 'address', 'reason','image','roles'
        )

class EditPatientSerializer(serializers.ModelSerializer):
    def create(self, validated_data):

        user = Patient.objects.create_user(
            username=validated_data['username'],
            first_name = validated_data['first_name'],
            email = validated_data['email'],
            image =  validated_data['image'],
            reason = validated_data['reason'],
            
        )

        return user

    class Meta:
        model = Patient
        fields = ('username','first_name','email','reason','image'
        )

# class BloodSerializer(serializers.ModelSerializer):
#      def create(self, validated_data):

#         user = CustomUser.objects.create_user(

#             blood_type = validated_data['blood_type'],
#             phone_number = validated_data['phone_number'],
#             first_name = validated_data['first_name'],
#             email = validated_data['email'],
#             image = validated_data['image'],
#             location = validated_data['location'],
            
#         )

#         return user
#      class Meta:
#         model = CustomUser
#         fields = ('first_name','email','image','location','phone_number'
#         ,'blood_type'
#         )
