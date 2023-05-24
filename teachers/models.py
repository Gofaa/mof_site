from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class Teachers(models.Model):
    full_name = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    academic_title = models.CharField(max_length=150)
    specialty = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='teacher_photo/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'tif', 'tiff'])])
    description = models.TextField()

    def __str__(self):
        return self.full_name

