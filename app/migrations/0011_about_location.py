# Generated by Django 4.2.4 on 2023-09-23 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_a_email_about_email_rename_a_name_about_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='location',
            field=models.CharField(default='Not Found', max_length=50),
        ),
    ]