# Generated by Django 4.2.9 on 2024-01-14 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0011_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='Invoice',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]