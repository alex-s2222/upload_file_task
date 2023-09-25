from django.urls import path

from . import views


urlpatterns = [
    path('upload', views.FileUploadView.as_view(), name='upload_file'),
    path('files', views.FilesView.as_view(), name='view_uploded_files')
]