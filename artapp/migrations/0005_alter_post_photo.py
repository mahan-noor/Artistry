# Generated by Django 3.2.4 on 2021-06-11 03:39

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artapp', '0004_auto_20210611_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='1920x1080'),
        ),
    ]
