from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from django.contrib.auth import get_user_model # If used custom user model
from .models import customUser
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from django.shortcuts import get_object_or_404



class CustomObtainAuthToken(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

class HospitalDetail(RetrieveAPIView):
    queryset = customUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    def get_object(self):
        UserName= self.kwargs.get("username")
        return get_object_or_404(customUser, username=UserName)