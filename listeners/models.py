from django.db import models

# Create your models here.


class Listeners(models.Model):
    full_name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='listeners/', null=True, blank=True)
    description = models.TextField()



    def __str__(self):
        return self.full_name