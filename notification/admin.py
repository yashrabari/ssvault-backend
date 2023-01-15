from django.contrib import admin
from .models import Device, ScheduleNotification, UserNotification


@admin.register(UserNotification)
class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ["title", "body", "is_read", "created_at"]
    

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ["user", "device_id", "device_type", "created_at"]


@admin.register(ScheduleNotification)
class ScheduleNotificationAdmin(admin.ModelAdmin):
    list_display = ["notification_name", "message", "scheduled_time", 
    "scheduled_type", "last_execution", "created_at", "is_active"]
    