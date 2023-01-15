from django.db.models import fields
from rest_framework import serializers
from .models import Device, UserNotification    

class UserNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotification
        exclude = ('user',)


class NotificationDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        exclude = ['user']

    def validate(self, validated_data):
        if not self.partial:
            try:
                Device.objects.get(user=self.context['request'].user, device_id=validated_data['device_id'])
                raise serializers.ValidationError("User Token already registered.")
            except Device.DoesNotExist:
                return validated_data
        return validated_data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return Device.objects.create(**validated_data)