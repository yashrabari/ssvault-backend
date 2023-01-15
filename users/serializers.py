
from rest_framework import serializers
from users import models


class BuddyInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BuddyInvitation
        exclude = ('user',)


class StorageCapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('email', 'name', 'storage', 'storage_left')


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'email', 'username', 'name','phone_number','location','storage','storage_left']


class BuddySerializerGET(serializers.ModelSerializer):
    buddy = CustomUserSerializer()
    class Meta:
        model = models.Buddy
        fields = '__all__'
