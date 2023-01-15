from users.models import User
from home.models import UUIDModel
from django.db import models
from djstripe.models import Subscription

class SubscriptionSetup(UUIDModel):
    """
    A model to represent the moment a subscription has been created
    """
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.SET_NULL,
        null=True
    )
