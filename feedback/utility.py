from django.core.mail import EmailMessage

from raspy_art_33412.settings import SENDGRID_EMAIL


def send_email(email, title, body):
    email_msg = EmailMessage(title, body, from_email=SENDGRID_EMAIL, to=[email])
    email_msg.content_subtype = "html"
    email_msg.send()
