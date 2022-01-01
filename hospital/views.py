from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView,ListAPIView,GenericAPIView
from django.contrib.auth import get_user_model # If used custom user model
from .models import customUser
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class CustomObtainAuthToken(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class CreateUserView(CreateAPIView):
    """
    A view that signup hospital.
    """
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

class HospitalDetail(RetrieveAPIView):
    """
    A view that returns the detail of hospital 
    """
    queryset = customUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    def get_object(self):
        UserName= self.kwargs.get("username")
        return get_object_or_404(customUser, username=UserName)

class ListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = customUser.objects.all()
    permission_classes = [permissions.AllowAny]

    


class countview(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        
        user_count = customUser.objects.count()
        content = {'user_count': user_count}
        return Response(content)