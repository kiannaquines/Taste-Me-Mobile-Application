# Generated by Django 4.2.1 on 2023-06-22 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cusine_app', '0003_alter_cusine_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cusine',
            name='cusine_image',
        ),
    ]
