# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20161026_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='site',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='placeofwork',
            name='site',
            field=models.URLField(default=''),
        ),
    ]