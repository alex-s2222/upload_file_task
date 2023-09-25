from django.db import models

# Create your models here.
class File(models.Model): 
    file = models.FileField(upload_to='files/%d_%m_%Y', null=True, blank=True)
    uploaded_at = models.DateTimeField(null=True, blank=True)
    processed = models.BooleanField(null=True, blank=True, default=False)
