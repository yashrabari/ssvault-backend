from django.contrib import admin
from files_folders import models

admin.site.register(models.File)
admin.site.register(models.Folder)
