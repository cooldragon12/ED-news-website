# Generated by Django 3.1 on 2021-01-30 10:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('News_web', '0004_auto_20210129_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 30, 10, 22, 48, 455285, tzinfo=utc)),
        ),
    ]
