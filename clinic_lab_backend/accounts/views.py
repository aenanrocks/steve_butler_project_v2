from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow anyone to access this view
