# Generated by Django 4.1.3 on 2024-03-17 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0009_alter_show_showtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='showtime',
            field=models.TimeField(default=datetime.datetime(2024, 3, 17, 17, 41, 44, 108396, tzinfo=datetime.timezone.utc), verbose_name='Showtime'),
        ),
    ]
