from django.urls import path,include
from rest_framework import routers
from files_folders import views

router = routers.DefaultRouter()
router.register('folders', views.FolderModelViewSet,basename='folders')
router.register('files', views.FileModelViewSet,basename='files')

urlpatterns = [
    path('', include(router.urls)),
    path('upload-file/',views.UploadFile.as_view(),),
    path('type-count/',views.GetFileTypeCount.as_view(),),

]