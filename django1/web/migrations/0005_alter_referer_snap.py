# Generated by Django 3.2.7 on 2021-09-23 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20210923_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referer',
            name='snap',
            field=models.TextField(verbose_name='snap'),
        ),
    ]