# Generated by Django 2.0.1 on 2018-01-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0014_remove_notes_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='color',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]