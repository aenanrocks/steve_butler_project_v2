from django.contrib import admin
from .models import Profile, Order
from .models import Notification

admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Notification)
