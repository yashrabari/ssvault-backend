from rest_framework import status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend

from .utility import send_email
from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackViewSet(ModelViewSet):
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes  = [TokenAuthentication]
    queryset = Feedback.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['responded']
    ordering_fields = ['responded']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['post'], permission_classes=[IsAdminUser])
    def respond(self, request):
        feedback = Feedback.objects.get(id=request.data.get('feedback'))
        send_email(email=feedback.user.email, title=request.data.get('title'), body=request.data.get('body'))
        feedback.responded = True
        feedback.save()
        return Response(status=status.HTTP_200_OK)
