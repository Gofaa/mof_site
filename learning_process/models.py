from django.db import models

# Create your models here.


class LearningProcess(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='media/learning_process/')

    def __str__(self):
        return self.title

