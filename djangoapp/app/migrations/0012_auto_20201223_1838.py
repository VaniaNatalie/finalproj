# Generated by Django 3.1.3 on 2020-12-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201223_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='diary_image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='diary_images', verbose_name='A Memorable Pic!'),
        ),
    ]