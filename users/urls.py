from django.urls import path,include
from rest_framework import routers
from users.views import (
    AcceptBuddyRequest,
    BuddyInvitationModelViewSet,
    CategoryModelViewSet,
    SetPasswordApiView,
    StorageCapacityViewSet,
    user_redirect_view,
    user_update_view,
    user_detail_view,
    ProfileModelViewSet,
    SendPasswordToken,
    VerifyOtpApiView,
    ResendPasswordToken,
    TwoFactorLogin
)

router = routers.DefaultRouter()
router.register('profile', ProfileModelViewSet,basename='profile')
router.register('user-category', CategoryModelViewSet)
router.register('buddy-invitation', BuddyInvitationModelViewSet,basename="buddy-invitation")
router.register('storage-capacity', StorageCapacityViewSet, basename="storage-capacity")


app_name = "users"
urlpatterns = [
    path('', include(router.urls)),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path('reset-password/send/',SendPasswordToken.as_view()),
    path('reset-password/verify/',VerifyOtpApiView.as_view()),
    path('reset-password/resend/',ResendPasswordToken.as_view()),
    path('set/password/', SetPasswordApiView.as_view()),
    path('buddy/accept/',AcceptBuddyRequest.as_view()),
    path('verify/2FA/',TwoFactorLogin.as_view())
]
