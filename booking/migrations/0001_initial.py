# Generated by Django 4.1.3 on 2024-03-17 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0002_film_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_code', models.CharField(max_length=100)),
                ('seat_num', models.CharField(max_length=25)),
                ('num_seats', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('show_date', models.DateField(null=True)),
                ('booked_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.show')),
            ],
        ),
    ]