# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-27 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0023_auto_20170227_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='land',
            field=models.CharField(blank=True, max_length=255, verbose_name='Non du Pays/PETR'),
        ),
        migrations.AlterField(
            model_name='project',
            name='shapefile',
            field=models.FileField(blank=True, null=True, upload_to='shapefile/', verbose_name='ou importer un ficher shape'),
        ),
    ]
