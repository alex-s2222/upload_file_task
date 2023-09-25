from rest_framework import serializers


from django.utils import timezone

from upload_file.models import File
from upload_file.handlers.process_file import proccessed_file
from upload_file.handlers.file_type import choise_type_file


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file','uploaded_at','processed',)

        extra_kwargs = {'uploaded_at': {'read_only': True}, 
                        'processed': {'read_only':True},}


    def create(self, validated_data):
        try:
            file_name = validated_data['file_name']
            file_type = choise_type_file(file_name)['type']
            print(file_type)

            uploaded_file = File(file=validated_data['file'],
                                uploaded_at=timezone.now())
            
            uploaded_file.save()
            file_id = uploaded_file.id
            
            if file_type == 'image':
                proccessed_file.delay(file_id)
            elif file_type == 'text':
                proccessed_file.delay(file_id)
            elif file_type == 'json':
                proccessed_file.delay(file_id)

            return uploaded_file
        
        except Exception as e:
            raise serializers.ValidationError({"error": str(e)})
