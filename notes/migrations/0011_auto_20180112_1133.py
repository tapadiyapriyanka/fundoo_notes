# Generated by Django 2.0.1 on 2018-01-12 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_auto_20180112_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='now',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 12, 11, 33, 10, 721439)),
        ),
    ]