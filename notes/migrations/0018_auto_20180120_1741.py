# Generated by Django 2.0.1 on 2018-01-20 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0017_auto_20180117_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='remainder',
        ),
        migrations.AddField(
            model_name='notes',
            name='mydate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
