from django.db import models
from django.contrib.auth import get_user_model

from home.models import UUIDModel


User = get_user_model()


class Feedback(UUIDModel):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='feedbacks'
    )
    title = models.CharField(
        max_length=255
    )
    message = models.TextField()
    responded = models.BooleanField(default=False)
