# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-13 07:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_image_author_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-pub_date'], 'verbose_name': 'My image', 'verbose_name_plural': 'Images'},
        ),
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Location'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
