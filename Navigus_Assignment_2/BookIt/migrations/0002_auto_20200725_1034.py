# Generated by Django 3.0.8 on 2020-07-25 05:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('BookIt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='name',
            field=models.CharField(default=datetime.datetime(2020, 7, 25, 5, 4, 31, 776656, tzinfo=utc), max_length=20, verbose_name='slot_name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slot',
            name='host_username',
            field=models.CharField(max_length=30, verbose_name='slot_host_username'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='status',
            field=models.IntegerField(choices=[('Booked', 'Booked')], verbose_name='slot_status'),
        ),
    ]
