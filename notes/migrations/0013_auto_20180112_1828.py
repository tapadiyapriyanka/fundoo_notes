# Generated by Django 2.0.1 on 2018-01-12 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0012_auto_20180112_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='now',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
