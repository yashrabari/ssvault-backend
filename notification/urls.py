from django.urls import path,include
from rest_framework import routers
from notification import views

router = routers.DefaultRouter()
router.register('user-notification', views.UserNotificationModelViewSet,basename='user-notification')
router.register("device", views.DeviceViewset, basename="device")

urlpatterns = [
    path('', include(router.urls)),

]   