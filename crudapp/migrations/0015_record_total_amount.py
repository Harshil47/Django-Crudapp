# Generated by Django 4.2.9 on 2024-01-14 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0014_customer_code_customer_state_record_cadr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='total_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
