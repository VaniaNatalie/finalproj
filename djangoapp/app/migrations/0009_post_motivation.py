# Generated by Django 3.1.3 on 2020-12-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20201223_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='motivation',
            field=models.CharField(help_text="It doesn't have to be something big, it can be looking at the sunrise, another episode of drama coming out or even listening to music on the way to work!", max_length=100, null=True, verbose_name='What motivates you for tomorrow?'),
        ),
    ]
