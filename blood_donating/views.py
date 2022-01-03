from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import CreateAPIView , ListAPIView,RetrieveUpdateDestroyAPIView
from .models import BloodType, Post
from .serializer import PostSerializer, BloodSerilaizer
from rest_framework import permissions

# Create your views here.

class PostViewSet(CreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

class GetViewSet(ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PostSerializer
    queryset =Post.objects.all().order_by("-time")
    # permission_classes = [permissions.IsAuthenticated]

class UpdateDestroyViewSet(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset =Post.objects.all().order_by("-time")
    # permission_classes = [permissions.IsAuthenticated]

class EditBlood(RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = BloodSerilaizer
    permission_classes = [permissions.AllowAny]
    queryset =BloodType.objects.all()
