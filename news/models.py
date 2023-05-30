from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='media/news/')
    publish_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publish_time']

    def __str__(self):
        return self.title
