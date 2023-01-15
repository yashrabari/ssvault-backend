from rest_framework import serializers

from home.api.v1.serializers import ProfileSerializerGET
from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    user = ProfileSerializerGET(required=False)

    class Meta:
        model = Feedback
        fields = '__all__'
