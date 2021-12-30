from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from django.contrib.auth import get_user_model # If used custom user model
from .models import customUser
from .serializers import UserSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomObtainAuthToken(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


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