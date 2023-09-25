from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from upload_file.serializers import FileSerializer
from upload_file.models import File


class FileUploadView(APIView):
    serializer_class = FileSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        try:
            if serializer.is_valid():
                uploaded_file_name = request.data['file'].name

                serializer.save(file_name=uploaded_file_name)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class FilesView(APIView):
    def get(self, request, format=None):
        try:
            files = File.objects.all()
            serializer = FileSerializer(files, many=True)
            return Response(serializer.data)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)