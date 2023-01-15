from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from core.utils import send_sms_via_twilio,generateOTP
from users.models import TwoFactorAuthentication

from home.api.v1.serializers import (
    SignupSerializer,
    UserSerializer,
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        if user.is_2FA:
            otp = generateOTP()
            two_fa = TwoFactorAuthentication.objects.filter(user=user).delete()
            TwoFactorAuthentication.objects.create(
                user=user,
                token=otp
            )
            send_sms_via_twilio(f'Your OTP is {otp}',user.phone_number)
            return Response({'msg':"OTP has been sent to your phone number."})
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})
