from django.shortcuts import render
from rest_framework import generics, permissions
from .serializer import AddSerializer,MyTokenObtainPairSerializer
from .models import Account
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.

class CustomObtainAuthToken(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class AddListView(generics.CreateAPIView):
    serializer_class = AddSerializer
    queryset = Account.objects.all()
    permission_classes = [permissions.AllowAny]

class DetailAddView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddSerializer
    queryset = Account.objects.all()
    
    def get_object(self):
        UserName= self.kwargs.get("username")
        return get_object_or_404(Account, username=UserName)
class ListView(generics.ListAPIView):
    serializer_class = AddSerializer
    queryset = Account.objects.all()
    permission_classes = [permissions.AllowAny]

class countview(APIView):
    """
    A view that returns the count of active users.
    """
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        print(request.data)
        user_count = Account.objects.count()
        content = {'user_count': user_count}
        return Response(content)