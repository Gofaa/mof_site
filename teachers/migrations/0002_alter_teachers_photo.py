# Generated by Django 4.2.1 on 2023-05-30 13:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teachers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teachers",
            name="photo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="media/teacher_photo/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["jpg", "jpeg", "png", "tif", "tiff"]
                    )
                ],
            ),
        ),
    ]
