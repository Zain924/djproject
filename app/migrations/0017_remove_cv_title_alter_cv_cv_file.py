# Generated by Django 4.2.4 on 2023-09-25 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='title',
        ),
        migrations.AlterField(
            model_name='cv',
            name='cv_file',
            field=models.FileField(upload_to='cv/'),
        ),
    ]
