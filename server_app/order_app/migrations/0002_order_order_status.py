# Generated by Django 4.2.1 on 2023-06-26 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.TextField(choices=[('Checkout', 'Checkout'), ('Pending', 'Pending')], default=('Checkout', 'Checkout')),
        ),
    ]
