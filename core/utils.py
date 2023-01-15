from django.core.mail import send_mail
from django.conf import settings
import math, random,uuid
from twilio.rest import Client

def send_custom_email(subject,message,recipient):
    subject = subject
    message = message
    send_mail(subject, message,
                settings.DEFAULT_FROM_EMAIL, [recipient])

def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'media/' + filename

def send_sms_via_twilio(body,msg_to):
    try:
        account_sid = settings.TWILIO_SID
        auth_token = settings.TWILIO_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                body=body,
                from_=settings.TWILIO_PHONE,
                to=msg_to
            )
        print(message)
    except Exception as e:
        print(e)