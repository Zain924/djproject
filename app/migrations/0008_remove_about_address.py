# Generated by Django 4.2.4 on 2023-09-22 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='address',
        ),
    ]