from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class ProtectedRouteView(APIView):
    permission_classes = [IsAuthenticated]  # Ensures this route requires authentication

    # Handle GET request
    def get(self, request):
        return Response({"message": "You have access to the protected route!"})

    # Handle POST request
    def post(self, request):
        # Process the data sent in the POST request here
        data = request.data
        return Response({"message": "POST request successful!", "data": data})