# Generated by Django 4.2.8 on 2023-12-29 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0005_remove_billing_billed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='bill_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='billing',
            name='final_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='billing',
            name='final_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='billing',
            name='material_rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='billing',
            name='transport_rate',
            field=models.FloatField(blank=True, null=True),
        ),
    ]