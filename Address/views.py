from django.shortcuts import render
from .models import Area,City,Address
from rest_framework import generics, permissions
from .serializer import AddAreaSerializer,AddCitySerializer,AddAddressSerializer

# Create your views here.


class AddAeraView(generics.CreateAPIView):
    serializer_class = AddAreaSerializer
    queryset = Area.objects.all()
    permission_classes = [permissions.AllowAny]
class AddCityView(generics.CreateAPIView):
    serializer_class = AddCitySerializer
    queryset = City.objects.all()
    permission_classes = [permissions.AllowAny]
class AddAddressView(generics.CreateAPIView):
    serializer_class = AddAddressSerializer
    queryset = Address.objects.all()
    permission_classes = [permissions.AllowAny]

