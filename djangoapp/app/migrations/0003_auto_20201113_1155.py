# Generated by Django 3.1.3 on 2020-11-13 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='profile_pic',
            new_name='image',
        ),
    ]
