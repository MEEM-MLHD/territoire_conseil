# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-26 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0041_auto_20170425_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referent',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='referent',
            name='function',
        ),
        migrations.RemoveField(
            model_name='referent',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='referent',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='referent',
            name='service',
        ),
        migrations.RemoveField(
            model_name='referent',
            name='structure',
        ),
        migrations.AlterField(
            model_name='project',
            name='begin',
            field=models.DateField(blank=True, help_text='JJ/MM/AAAA', null=True, verbose_name='Date de d\xe9but de projet'),
        ),
        migrations.AlterField(
            model_name='project',
            name='end',
            field=models.DateField(blank=True, help_text='JJ/MM/AAAA', null=True, verbose_name='Date pr\xe9visionnelle de fin de projet'),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True, help_text='Lien URL', verbose_name='Pour en savoir plus'),
        ),
    ]
