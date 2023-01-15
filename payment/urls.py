from django.urls import path,include
from rest_framework import routers

from .views import SubscriptionViewSet

router = routers.DefaultRouter()
router.register("payments", SubscriptionViewSet, basename="payments")

urlpatterns = [
    path('', include(router.urls)),
]