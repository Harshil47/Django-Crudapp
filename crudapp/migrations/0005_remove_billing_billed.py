# Generated by Django 4.2.8 on 2023-12-29 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0004_billing_orders_billed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billing',
            name='billed',
        ),
    ]
