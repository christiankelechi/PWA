# Generated by Django 4.2.11 on 2024-04-08 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, max_length=2000, null=True)),
                ('file', models.FileField(upload_to='image_media')),
            ],
        ),
    ]
