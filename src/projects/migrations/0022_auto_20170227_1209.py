# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-27 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_auto_20170130_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, verbose_name='Pour en savoir plus (lien URL)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='comments',
            field=models.TextField(blank=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='referent',
            name='service',
            field=models.CharField(blank=True, help_text='Eviter les sigles', max_length=255, verbose_name='Service'),
        ),
    ]
