# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-20 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0035_referent_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='funding_departmental',
            field=models.CharField(blank=True, max_length=255, verbose_name='Financement d\xe9partemental'),
        ),
        migrations.AddField(
            model_name='project',
            name='funding_european',
            field=models.CharField(blank=True, max_length=255, verbose_name='Financement europ\xe9en'),
        ),
        migrations.AddField(
            model_name='project',
            name='funding_national',
            field=models.CharField(blank=True, max_length=255, verbose_name='Financement national'),
        ),
        migrations.AddField(
            model_name='project',
            name='funding_other',
            field=models.CharField(blank=True, max_length=255, verbose_name='Autre financement'),
        ),
        migrations.AddField(
            model_name='project',
            name='funding_regional',
            field=models.CharField(blank=True, max_length=255, verbose_name='Financement r\xe9gional'),
        ),
    ]
