# Generated by Django 2.2.3 on 2019-08-04 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='query',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='query_id',
        ),
    ]
