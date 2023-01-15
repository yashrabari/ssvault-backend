from users.models import Category
from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.utils.translation import ugettext_lazy as _
from allauth.account import app_settings as allauth_settings
from allauth.account.forms import ResetPasswordForm
from allauth.utils import email_address_exists, generate_unique_username
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from rest_auth.serializers import PasswordResetSerializer
from users.serializers import BuddySerializerGET


from payment.serializers import SubscriptionSerializer

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password','phone_number')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            },
            'email': {
                'required': True,
                'allow_blank': False,
            }
        }

    def _get_request(self):
        request = self.context.get('request')
        if request and not isinstance(request, HttpRequest) and hasattr(request, '_request'):
            request = request._request
        return request

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def create(self, validated_data):
        user = User(
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            username=generate_unique_username([
                validated_data.get('name'),
                validated_data.get('email'),
                'user'
            ]),
            phone_number = validated_data.get('phone_number'),
        )
        user.set_password(validated_data.get('password'))
        user.save()
        request = self._get_request()
        setup_user_email(request, user, [])
        return user

    def save(self, request=None):
        """rest_auth passes request so we must override to accept it"""
        return super().save()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProfileSerializerGET(serializers.ModelSerializer):
    # category = CategorySerializer(many=True)
    buddy = BuddySerializerGET(many=True)
    subscription = SubscriptionSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'name','phone_number','location',
        'verification_period','buddy','storage','storage_left', 'profile_picture',
        'subscription', 'customer_account']

class ProfileSerializerPOST(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True, many=True)

    user_data = serializers.JSONField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'email', 'username','name', 'phone_number','location',
                'verification_period','storage','storage_left', 
                'profile_picture', 'user_data']

        extra_kwargs = {'username': {'required': False}}

    def create(self, validated_data):
        user = self.context['request'].user
        user_data = validated_data['user_data']
        # category = validated_data['user_data'].pop('category')
        profile_picture = validated_data.pop('profile_picture', '')
        if profile_picture:
            user_data['profile_picture']= profile_picture
        user = User.objects.create(**user_data)
        # user.category.set(category)
        return user

    def update(self, instance, validated_data):
        user_data = validated_data['user_data']
        # category = validated_data['user_data'].pop('category')
        profile_picture = validated_data.pop('profile_picture', '')
        if profile_picture:
            user_data['profile_picture']= profile_picture
        # instance.category.set(category)
        for k, v in user_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name','phone_number','location','storage','storage_left']


class PasswordSerializer(PasswordResetSerializer):
    """Custom serializer for rest_auth to solve reset password error"""
    password_reset_form_class = ResetPasswordForm
 