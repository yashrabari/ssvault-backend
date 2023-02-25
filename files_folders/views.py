from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.db.models import Count, Sum
from files_folders import serializers,models
import logging


class FolderModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get','post', 'put','delete']
    serializer_class = serializers.FolderSerializer
    
    def get_queryset(self):
        print('AAAAAAAAAAAAAAAAA')
        return models.Folder.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        print('AHHHHHHHHHHHHH')
        serializer.save(user=self.request.user)

class FileModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get','delete']
    serializer_class = serializers.FileSerializer
    
    def get_queryset(self):
        return models.File.objects.filter(user=self.request.user)

class UploadFile(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        try:
            user = request.user
            if user.storage_left >= user.storage:
                return Response({"message":"Your storage is full."},status=status.HTTP_201_CREATED)
            file_count = models.File.objects.filter(user=user).values('extension').annotate(count=Count('extension')).annotate(size=Sum('size'))
            # if file_count >= 2:
            #     return Response({"message":"You Can't Upload more than 2 Files."},status=status.HTTP_201_CREATED)
            file = request.FILES['file']
            logging.debug("Oh hai!")
            folder = models.Folder.objects.get(id=request.data['folder_id'])
            size = float(file.size)/1000000
            file_upload = models.File.objects.create(
                name = file.name,
                extension = file.content_type,
                folder = folder,
                file = file,
                user = user,
                size = size
            )
            user.storage_left += size
            user.save()
            return Response({"message":"Successfully Uploaded file."},status=status.HTTP_201_CREATED)
        except Exception as e:
             return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class GetFileTypeCount(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        try:
            user = request.user 
            qs = models.File.objects.filter(user=user).values('extension').annotate(count=Count('extension')).annotate(size=Sum('size'))
            return Response({"result":qs},status=status.HTTP_201_CREATED)
        except Exception as e:
             return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
