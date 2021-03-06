# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-27 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_remove_project_other_perimeter'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_leader_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Nom du porteur de projet'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_leader_type',
            field=models.CharField(blank=True, choices=[('public', 'Public'), ('private', 'Priv\xe9')], max_length=255, verbose_name='Type de porteur de projet'),
        ),
    ]
