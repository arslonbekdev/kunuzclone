# Generated by Django 5.0.1 on 2024-04-01 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0004_contact_alter_news_publish_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='publish_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 1, 10, 48, 41, 142260, tzinfo=datetime.timezone.utc)),
        ),
    ]
