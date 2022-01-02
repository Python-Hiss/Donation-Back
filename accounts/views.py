from django.shortcuts import render
from rest_framework import generics, permissions
from .serializer import AddSerializer,MyTokenObtainPairSerializer,EditSerializer
from .models import UserAccount
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class CustomObtainAuthToken(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class AddListView(generics.CreateAPIView):
    serializer_class = AddSerializer
    queryset = UserAccount.objects.all()
    permission_classes = [permissions.AllowAny]

class DetailAddView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EditSerializer
    queryset = UserAccount.objects.all()
    permission_classes = [permissions.AllowAny]
    
    def get_object(self):
        UserName= self.kwargs.get("username")
        return get_object_or_404(UserAccount, username=UserName)
class ListView(generics.ListAPIView):
    serializer_class = AddSerializer
    queryset = UserAccount.objects.all()
    permission_classes = [permissions.AllowAny]

class countview(APIView):
    """
    A view that returns the count of active users.
    """
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        print(request.data)
        user_count = UserAccount.objects.count()
        content = {'user_count': user_count}
        return Response(content)