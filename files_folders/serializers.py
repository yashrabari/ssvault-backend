from rest_framework import serializers
from files_folders import models
from home.api.v1.serializers import UserSerializer



class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = '__all__'

class FolderSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False, read_only=True)
    parent_folder = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()

    def get_parent_folder(self, obj):
        if obj:
            if obj.parent:
                return FolderSerializer(obj.parent).data
        return None

    def get_files(self,obj):
        return FileSerializer(models.File.objects.filter(folder=obj),many=True).data

    class Meta:
        model = models.Folder
        fields = '__all__'

