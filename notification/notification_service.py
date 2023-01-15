from django.conf import settings
from pyfcm import FCMNotification


class FCMServices():
    def __init__(self):
        self.push_service = FCMNotification(api_key=settings.FIREBASE_API_KEY)

    def send_fcm_notification(self, device_tokens, message_title, message_body, data):
        try:
            if isinstance(device_tokens, list):
                device_tokens = self.clean_invalid_device_tokens(device_tokens)
                result = self.push_service.notify_multiple_devices(
                    registration_ids=device_tokens, message_title=message_title, 
                    message_body=message_body, data_message=data
                    )
            else:
                result = self.push_service.notify_single_device(
                    registration_id=device_tokens, message_title=message_title, 
                    message_body=message_body, data_message=data
                )

            return result.get('success', 0)
        except Exception:
            return 0


    def clean_invalid_device_tokens(self, device_tokens):
        try:
            return self.push_service.clean_registration_ids(device_tokens)
        except Exception:
            return []
