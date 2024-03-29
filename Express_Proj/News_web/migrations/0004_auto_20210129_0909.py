# Generated by Django 3.1 on 2021-01-29 01:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('News_web', '0003_auto_20201201_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='trending',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 29, 1, 9, 50, 209280, tzinfo=utc)),
        ),
    ]
