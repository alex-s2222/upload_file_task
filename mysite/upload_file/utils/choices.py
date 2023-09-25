from django.db.models import TextChoices


class FileType(TextChoices):
    JSON_FILE = '.json'
    TEXT_FILE = ('.word', '.txt')
    IMAGE_FILE = ('.jpg', '.png')
