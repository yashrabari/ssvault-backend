from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from core.utils import send_custom_email
from .models import Buddy, BuddyInvitation, Category, EmailTokenVerification,PasswordReset, TwoFactorAuthentication
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from home.api.v1.serializers import CategorySerializer, ProfileSerializerGET, ProfileSerializerPOST, UserSerializer
from core.utils import generateOTP
from users import serializers
from rest_framework.authtoken.models import Token
from users.models import User
User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

class ProfileModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['put','get', 'post']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProfileSerializerGET
        if self.action == 'retrieve':
            return ProfileSerializerGET
        return ProfileSerializerPOST

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class CategoryModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SendPasswordToken(APIView):
    def post(self,request):
        try:
            email = request.data['email']
            password_reset = PasswordReset.objects.filter(user__email=email)
            if password_reset.exists():
                    password_reset=password_reset.first()
                    send_custom_email(
                    "Password Reset Token",
                    f"Your Token for Password reset is {password_reset.token}",
                    password_reset.user.email)
                    return Response({"message":"Successfully Token sent."},status=status.HTTP_201_CREATED)
            token = generateOTP()
            user= User.objects.filter(email=email)
            if user.exists():
                user = user.first()
                PasswordReset.objects.create(
                    user = user,
                    token =token 
                )
                send_custom_email(
                    "Password Reset Token",
                    f"Your Token for Password reset is {token}",
                    user.email)
                return Response({"message":"Successfully Token sent."},status=status.HTTP_201_CREATED)
            return Response({"message":"User not found."},status=status.HTTP_201_CREATED)
            
        except Exception as e:
             return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class VerifyOtpApiView(APIView):

    def post(self,request):
        try:
            token = request.data['token']
            user_verify = PasswordReset.objects.filter(user__email = request.data['email'])
            if user_verify.exists():
                user_verify = user_verify.first()
                if token == user_verify.token:
                    user_verify.delete()
                    return Response({"message":"Token Verified."},status=status.HTTP_201_CREATED)
            return Response({"message":"Wrong Token or doesn't exist."},status=status.HTTP_201_CREATED)
        except Exception as e:
             return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class SetPasswordApiView(APIView):

    def post(self,request):
        try:
            user = User.objects.get(email=request.data['email'])
            user.set_password(request.data['password'])
            user.save()
            return Response({"message":"Password updated successfully!."}, status=status.HTTP_201_CREATED)
        except Exception as e:
             return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

class TwoFactorLogin(APIView):
    def post(self,request):
        try:
            token = request.data['token']
            user_verify = TwoFactorAuthentication.objects.filter(token=token)
            if user_verify.exists():
                user_verify = user_verify.first()
                token, created = Token.objects.get_or_create(user=user_verify.user)
                return Response({"token": token.key})
            return Response({"message":"Wrong Token."},status=status.HTTP_201_CREATED)
            
        except Exception as e:
             return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

class ResendPasswordToken(APIView):
    def post(self,request):
        try:
            email = request.data['email']
            user_verify = PasswordReset.objects.filter(user__email = email)
            if user_verify.exists():
                user_verify = user_verify.first()
                send_custom_email(
                    "Password Reset Token",
                    f"Your Token for Password reset is {user_verify.token}",
                    user_verify.user.email)
                return Response({"message":"Successfully resend Token"},status=status.HTTP_201_CREATED)
            return Response({"message":"User Doesn't exist"},status=status.HTTP_201_CREATED)
            
        except Exception as e:
             return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class BuddyInvitationModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.BuddyInvitationSerializer

    def get_queryset(self):
        return BuddyInvitation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AcceptBuddyRequest(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            if self.request.user.buddy.count() < 3:
                buddy_invite = BuddyInvitation.objects.filter(id=request.data['buddy_invite'],user=request.user)
                if not buddy_invite.exists():
                    return Response({"message":"No invite found."},status=status.HTTP_201_CREATED)
                buddy_invite = buddy_invite.first()
                user = User.objects.filter(email=buddy_invite.email)
                if not user.exists():
                    return Response({"message":"User hasn't signup at the system yet."},status=status.HTTP_201_CREATED)
                user = user.first()
                buddy,created = Buddy.objects.get_or_create(
                    buddy=user,
                    relationship=buddy_invite.relationship
                )
                buddy_invite.user.buddy.add(buddy)
                buddy_invite.is_accepted = True
                buddy_invite.save()
                return Response({"message":"Successfully Accepted the invite."},status=status.HTTP_201_CREATED)
            return Response({"message":"You already have 3 active buddies."},status=status.HTTP_201_CREATED)
        except Exception as e:
             return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class StorageCapacityViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    serializer_class = serializers.StorageCapacitySerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)