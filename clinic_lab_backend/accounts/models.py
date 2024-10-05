from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        from .models import Profile
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('clinic', 'Clinic'),
        ('lab', 'Lab'),
    )
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username
    
class Order(models.Model):
    STATUS_CHOICES = (
        ('submitted', 'Submitted'),
        ('pending_review', 'Pending Review'),
        ('in_progress', 'In Progress'),
        ('on_hold', 'On Hold'),
        ('completed', 'Completed'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )
    DELIVERY_CHOICES = (
        ('pickup', 'Pickup'),
        ('email', 'Email'),
        ('post', 'Post'),
    )
    
    clinic = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    lab = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lab_orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    delivery_method = models.CharField(max_length=10, choices=DELIVERY_CHOICES, default='email')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.recipient.username} - {self.message}"
