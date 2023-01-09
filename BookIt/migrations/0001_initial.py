# Generated by Django 3.0.8 on 2020-07-25 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='event name', max_length=20)),
                ('user', models.CharField(help_text='host user name', max_length=40)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Booked', 'Booked')], help_text='status of slot', max_length=10)),
                ('date', models.DateField(help_text='date for slot')),
                ('start_time', models.TimeField(help_text='slot start time')),
                ('end_time', models.TimeField(help_text='slot end time')),
                ('created_at', models.TimeField(auto_now_add=True, help_text='slot created time')),
                ('attendee', models.CharField(blank=True, help_text='attendee username', max_length=30)),
                ('user_id', models.ForeignKey(help_text='host username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'slot_data',
                'verbose_name_plural': 'slot_datas',
            },
        ),
    ]