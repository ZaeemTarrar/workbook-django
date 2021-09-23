# Generated by Django 3.2.7 on 2021-09-23 05:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RefererModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30, verbose_name='referer.firstname')),
                ('middlename', models.CharField(max_length=30, verbose_name='referer.middleware')),
                ('lastname', models.CharField(max_length=30, verbose_name='referer.lastname')),
                ('cnic', models.CharField(max_length=30, verbose_name='referer.cnic')),
                ('designation', models.CharField(max_length=30, verbose_name='referer.designation')),
                ('address', models.CharField(max_length=30, verbose_name='referer.address')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='referer.date.created')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='referer.date.updated')),
            ],
            options={
                'db_table': 'referer',
            },
        ),
    ]
