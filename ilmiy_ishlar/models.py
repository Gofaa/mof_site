from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class ScientificWork(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    file = models.FileField(upload_to='media/ilmiy_ishlar/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx', 'pdf', 'ppt', 'txt'])])

    def __str__(self):
        return self.title