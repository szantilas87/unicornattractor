# Generated by Django 2.2.3 on 2019-08-22 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='premium',
            field=models.BooleanField(default=True),
        ),
    ]
