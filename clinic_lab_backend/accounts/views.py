from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order, Notification
from .serializers import UserSerializer, OrderSerializer, NotificationSerializer

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
    
# List all orders (for the logged-in user) and create new orders
class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(clinic=self.request.user)  # Return only orders for the authenticated clinic

    def perform_create(self, serializer):
        serializer.save(clinic=self.request.user)  # Automatically assign the authenticated user to the clinic field

# Retrieve, update, or delete a specific order
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(clinic=self.request.user)  # Ensure only clinic orders are accessible
    
# List all notifications for the logged-in user
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)

# Mark a notification as read
class NotificationDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)