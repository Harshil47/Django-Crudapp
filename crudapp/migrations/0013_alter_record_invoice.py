# Generated by Django 4.2.9 on 2024-01-14 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0012_record_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='Invoice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]