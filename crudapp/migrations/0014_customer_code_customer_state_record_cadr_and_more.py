# Generated by Django 4.2.9 on 2024-01-14 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0013_alter_record_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='code',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='Cadr',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='Cname',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='Sadr',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='code',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='state',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='adr',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Pname',
            field=models.CharField(max_length=100),
        ),
    ]