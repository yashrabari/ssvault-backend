import logging
from django.core.management.base import BaseCommand
from django.core.management import CommandError
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta
from notification.models import ScheduleNotification
from notification.notification_service import FCMServices
from users.models import Buddy, BuddyInvitation
from users.models import User

# from home.sms import SMS

User = get_user_model()
logger = logging.getLogger(__name__)
UTC_TIMEZONE = timezone.utc


class ScheduleValidation(object):

    def __init__(self, schedule):
        self.schedule = schedule
        self.date_today = datetime.now(tz=UTC_TIMEZONE).date()

    def validate_daily(self):
        if (self.schedule.last_execution + timedelta(days=1)).date() <= self.date_today:
            return True
        return False

    def _validate(self):
        if self.schedule.scheduled_type == ScheduleNotification.EVERY_DAY:
            return self.validate_daily()
        else:        
            return False

    def validate(self):
        if not self.schedule.last_execution:
            return True
        return self._validate()


class PushNotification(object):

    def __init__(self, schedule):
        self.schedule = schedule
        self.users = self.get_users()

    def get_users(self):
        if self.schedule.user_type == ScheduleNotification.BUDDY:
            return BuddyInvitation.buddy_users()
        elif self.schedule.user_type == ScheduleNotification.PRIME:
            return User.prime_users()
        else:
            return User.all_users()
    
    def send(self):
        data = {
            "type": "Information"
        }
        for buddy_obj in self.users:
            user = User.objects.get(email=buddy_obj.buddy.email)
            try:
                if buddy_obj.buddy:
                    FCMServices().send_fcm_notification(
                        user.device.device_id,
                        self.schedule.notification_name,
                        self.schedule.message,
                        data
                    )
                else:
                    logger.exception("No email for this user: {0}".format(user.username))
            except Exception as ex:
                logger.exception("Failed to send SMS to {0}, Exception: {1}".format(str(user.phone_number), str(ex)))
        self.schedule.last_execution = datetime.now(tz=UTC_TIMEZONE)
        self.schedule.save()


class Command(BaseCommand):
    help = 'Send Push notification to users'

    @property
    def time_range(self):
        # Filter with 5 minute time range
        current_time = datetime.now(tz=UTC_TIMEZONE)
        before_time = (current_time - timedelta(minutes=3)).strftime("%H:%M:%S")
        after_time = (current_time + timedelta(minutes=2)).strftime("%H:%M:%S")
        return before_time, after_time

    @property
    def current_schedules(self):
        schedules = ScheduleNotification.objects.filter(
            is_active=True, scheduled_time__range=self.time_range
        )
        return schedules

    def handle(self, *args, **options):
        # try:
        if self.current_schedules:
            self.stdout.write("Send SMS notification started!")
            for schedule in self.current_schedules:
                if ScheduleValidation(schedule).validate():
                    self.stdout.write("Executing the schedule: {0}".format(schedule.notification_name))
                    PushNotification(schedule).send()
            self.stdout.write("Send SMS notification completed!")
        self.stdout.write("No notification in process!")
        # except Exception as ex:
        #     self.stdout.write("Exception occurred in Send SMS Notification: {0}".format(str(ex)))
