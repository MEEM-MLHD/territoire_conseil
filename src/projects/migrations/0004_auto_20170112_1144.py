# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-12 11:44
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command

def loadfixture(apps, schema_editor):
    call_command('loaddata', 'data.json')


def backward(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20170112_1017'),
    ]

    operations = [
        migrations.RunPython(loadfixture, backward),
    ]