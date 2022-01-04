from .models import BloodType
from .models2 import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id",'patient', 'title',"time","text","publish"]

class BloodSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = BloodType
        fields = ['blood_type','description']

class AddBloodSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodType
        fields = ('id','blood_type','description')

