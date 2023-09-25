from celery import shared_task
from upload_file.models import File
import time

@shared_task
def proccessed_file(file_id):
    file = File.objects.get(id=file_id)
    #обработка файла
    time.sleep(30)

    file.processed = True
    file.save()
