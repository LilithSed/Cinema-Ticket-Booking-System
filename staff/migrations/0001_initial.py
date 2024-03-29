# Generated by Django 4.1.3 on 2024-03-16 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100, verbose_name='Movie Name')),
                ('movie_genre', models.CharField(blank=True, max_length=100, null=True)),
                ('movie_lang', models.CharField(blank=True, max_length=100, null=True, verbose_name='Language')),
                ('movie_year', models.IntegerField(blank=True, null=True, verbose_name='Year')),
                ('movie_plot', models.TextField(blank=True, help_text='movie plot here ', null=True, verbose_name='Plot')),
                ('url', models.URLField(blank=True, null=True)),
                ('date_added', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(null=True, verbose_name='End Date')),
                ('price', models.PositiveIntegerField(verbose_name='Ticket Price')),
                ('showtime', models.TimeField(blank=True, null=True, verbose_name='Showtime')),
                ('room', models.PositiveIntegerField(verbose_name='Room')),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.film', verbose_name='Movie')),
            ],
        ),
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Banner Image URL')),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.film', verbose_name='Movie')),
            ],
        ),
    ]
