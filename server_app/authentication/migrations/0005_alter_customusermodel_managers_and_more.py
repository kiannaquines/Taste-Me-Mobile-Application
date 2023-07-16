# Generated by Django 4.2.1 on 2023-06-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customusermodel',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
