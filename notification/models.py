from pickle import TRUE
from django.db import models
from users.models import User


class UserNotification(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    user = models.ManyToManyField(User)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Device(models.Model):
    IOS=1
    ANDROID=2
    WEB=3

    DEVICE_TYPE = (
        (IOS, 'IOS'),
        (ANDROID, 'ANDROID'),
        (WEB, 'WEB'),
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="device"
    )
    device_id = models.TextField()
    device_type = models.PositiveSmallIntegerField(
        choices=DEVICE_TYPE
    )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}-{}'.format(str(self.user.id), str(self.device_type))


class ScheduleNotification(models.Model):
    # Schedule types
    EVERY_DAY = 1
    SCHEDULE_TYPE = (
        (EVERY_DAY, "Every Day"),
        
    )
    PRIME = 1
    BUDDY = 2
    DEFAULT = 0

    USER_TYPES = (
        (DEFAULT, "----"),
        (PRIME, "Prime"),
        (BUDDY, "Buddy")
    )

    notification_name = models.CharField(
        max_length=300
    )
    message = models.TextField(
        blank=True, null=True
    )
    is_active = models.BooleanField(
        default=False
    )
    users = models.ManyToManyField(User)
    scheduled_time = models.TimeField()
    scheduled_type = models.PositiveSmallIntegerField(
        choices=SCHEDULE_TYPE
    )
    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPES, default=DEFAULT
    )
    last_execution = models.DateTimeField(
        blank=True, null=True
    )
    created_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.notification_name

    @classmethod
    def active_schedules(cls):
        return cls.objects.filter(is_active=True)