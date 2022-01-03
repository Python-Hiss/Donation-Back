from django.shortcuts import render
from .models import BloodType
from rest_framework import generics, permissions
from .serializer import AddBloodSerializer

# Create your views here.


class AddBloodView(generics.CreateAPIView):
    serializer_class = AddBloodSerializer
    queryset = BloodType.objects.all()
    permission_classes = [permissions.AllowAny]