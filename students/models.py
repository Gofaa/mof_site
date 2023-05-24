from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.


class ActiveStudents(models.Model):
    full_name = models.CharField(max_length=150)
    study_group = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='active_students/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'tif', 'tiff'])])
    description = models.TextField()

    def __str__(self):
        return self.full_name




class InactiveStudents(models.Model):
    full_name = models.CharField(max_length=150)
    study_group = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='inactive_students/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'tif', 'tiff'])])
    description = models.TextField()

    def __str__(self):
        return self.full_name


