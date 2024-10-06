from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Order, Notification
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
        username=validated_data['username'],
        email=validated_data['email'],
        password=validated_data['password']
        )
        return user

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'clinic', 'lab', 'status', 'delivery_method', 'notes', 'created_at', 'updated_at']
        read_only_fields = ['clinic', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        # Update the order
        instance = super().update(instance, validated_data)

        # Notify the clinic about the order status update
        channel_layer = get_channel_layer()
        notification_message = f"Order {instance.id} updated to {instance.status}"

        # Send the notification to the user's group
        async_to_sync(channel_layer.group_send)(
            f"user_{instance.clinic.id}",  # Send to the clinic's group
            {
                'type': 'send_notification',
                'message': notification_message
            }
        )

        return instance

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'