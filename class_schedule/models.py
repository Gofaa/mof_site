from django.db import models

# Create your models here.

class ClassSchedule(models.Model):
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    GROUP_CHOICES = (
        ("AX", "AX"),
        ('KIF', 'KIF'),
        ('TELEKOM', 'TELEKOM'),
        ('RADIO', 'RADIO'),
    )

    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    time = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    group = models.CharField(max_length=20, choices=GROUP_CHOICES)

    def __str__(self):
        return f"{self.group} - {self.day} - {self.time} - {self.course}"

