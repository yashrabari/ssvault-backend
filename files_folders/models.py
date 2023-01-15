from operator import mod
from django.db import models
from users.models import User
from core.utils import get_file_path


class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('Folder',
                                on_delete=models.CASCADE,
                                null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

class File(models.Model):
    name = models.CharField(max_length=255)
    extension = models.CharField(max_length=20)
    folder = models.ForeignKey(Folder,on_delete=models.CASCADE,
                        null=True,blank=True)
    uploaded_on = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=get_file_path)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    size = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.name