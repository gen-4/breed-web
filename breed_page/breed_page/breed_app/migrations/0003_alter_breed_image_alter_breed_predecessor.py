# Generated by Django 4.1 on 2022-08-17 16:04

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('breed_app', '0002_alter_breed_image_alter_breed_predecessor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=pathlib.PurePosixPath('/home/anton/Documentos/projects/python/breed-web/breed_page/breed_page/static')),
        ),
        migrations.AlterField(
            model_name='breed',
            name='predecessor',
            field=models.ManyToManyField(blank=True, null=True, related_name='breed_to_predecessors', to='breed_app.breed'),
        ),
    ]
