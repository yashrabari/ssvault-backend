from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from .models import Device, UserNotification
from rest_framework.response import Response
from rest_framework import status

from .serializers import NotificationDeviceSerializer, UserNotificationSerializer

class UserNotificationModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserNotificationSerializer

    def get_queryset(self):
        return UserNotification.objects.filter(user=self.request.user)
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeviceViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'patch']
    serializer_class = NotificationDeviceSerializer
    queryset = Device.objects.all()
    message = "Notification device added successfully"

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        try:
            device_obj = Device.objects.get(user=request.user)
            serializer = self.serializer_class(device_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.data, status.HTTP_201_CREATED)
        except Exception as e:
            print(e, "ee")
            return Response({}, status.HTTP_201_CREATED)

