import os
import uuid;
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


def get_user_folder(instance):
    return "".join(instance.username).lower() + str(instance.id)


def user_document_path(instance, filename):
    extension = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{extension}"
    return os.path.join(instance.__class__.__name__.lower(), get_user_folder(instance), filename)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    def clean(self):
        if not Category.objects.filter(name__icontains=self.name).exists():
            super(Category, self).clean()
        else:
            raise ValidationError(f"{self.name} category already exist.")
        

VERIFICATION_PERIOD = (
    ("One Week", "One Week"),
    ("Two Week", "Two Week"),
    ("One Month", "One Month"),
)


class User(AbstractUser):
    name = models.CharField(_("Name of User"), blank=True, null=True, max_length=255)
    phone_number = models.CharField(max_length=20,null=True)
    is_2FA = models.BooleanField(default=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    stripe_id = models.CharField(max_length=50,null=True,blank=True)
    # category = models.ManyToManyField(Category)
    verification_period = models.CharField(max_length=255,choices=VERIFICATION_PERIOD,default='')
    storage = models.FloatField(default=100)
    storage_left = models.FloatField(default=0)
    buddy= models.ManyToManyField('Buddy',blank=True)
    default_payment_method = models.CharField(max_length = 255,null=True)
    profile_picture = models.FileField(
        upload_to=user_document_path, blank=True, null=True
    )
    subscription = models.ForeignKey(
        'djstripe.Subscription', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="The user's Stripe Subscription object, if it exists"
    )
    customer_account = models.ForeignKey(
        'djstripe.Customer', null=True, blank=True, on_delete=models.SET_NULL,
        help_text="The user's Stripe Customer object, if it exists"
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    @classmethod
    def prime_users(cls):
        return cls.objects.filter(active=True)

    @classmethod
    def all_users(cls):
        return cls.objects.filter(active=True)

    @property
    def subscription_name(self):
        try:
            return self.subscription.plan.product.name
        except Exception as e:
            return "-"
            


class Buddy(models.Model):
    buddy = models.ForeignKey(User,on_delete=models.CASCADE,related_name='buddy_buddy',null=True)
    relationship = models.CharField(max_length=255)

    @classmethod
    def buddy_users(cls):
        return cls.objects.all()

    def __str__(self) -> str:
        return self.buddy.email

class EmailTokenVerification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.user.email

class PasswordReset(EmailTokenVerification):
    pass

class TwoFactorAuthentication(EmailTokenVerification):
    pass

class BuddyInvitation(models.Model):
    email = models.EmailField()
    is_accepted = models.BooleanField(default=False)
    relationship = models.CharField(max_length=255,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    @classmethod
    def buddy_users(cls):
        return cls.objects.filter(is_accepted=True)

    def __str__(self) -> str:
        return self.email

