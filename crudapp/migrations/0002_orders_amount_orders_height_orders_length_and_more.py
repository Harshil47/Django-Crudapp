# Generated by Django 4.2.8 on 2023-12-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='length',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='width',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
