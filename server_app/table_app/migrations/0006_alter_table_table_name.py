# Generated by Django 4.2.1 on 2023-05-30 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table_app', '0005_alter_table_table_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='table_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
