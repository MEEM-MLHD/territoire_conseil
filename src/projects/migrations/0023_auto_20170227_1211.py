# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-27 12:11
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_auto_20170227_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='shapefile',
            field=models.FileField(blank=True, null=True, upload_to='shapefile/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='geom',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326, verbose_name='Dessiner le contour du projet'),
        ),
    ]
