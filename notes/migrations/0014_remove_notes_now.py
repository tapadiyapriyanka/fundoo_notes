# Generated by Django 2.0.1 on 2018-01-13 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0013_auto_20180112_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='now',
        ),
    ]
