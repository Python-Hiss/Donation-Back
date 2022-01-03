from django.shortcuts import render
from rest_framework.generics import CreateAPIView , ListAPIView,RetrieveUpdateDestroyAPIView
from .models import Post
from .serializer import PostSerializer
from rest_framework import permissions

# Create your views here.

class PostViewSet(CreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

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
