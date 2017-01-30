# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-12 10:03
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('insee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='InterventionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=255)),
                ('intervention', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Intervention')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('epci_name', models.CharField(max_length=255)),
                ('epci_siren', models.CharField(max_length=255)),
                ('town_name', models.CharField(max_length=255)),
                ('town_insee', models.CharField(max_length=255)),
                ('other_perimeter', models.CharField(max_length=255)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('description', models.TextField()),
                ('ddt_reference_name', models.CharField(max_length=255)),
                ('ddt_reference_service', models.CharField(max_length=255)),
                ('interventions_others', models.CharField(max_length=255)),
                ('themes', models.TextField()),
                ('manager_other', models.CharField(max_length=255)),
                ('manager_detail', models.TextField()),
                ('structure_challenges', models.TextField()),
                ('obstables', models.TextField()),
                ('contact_firstname', models.CharField(max_length=255)),
                ('contact_lastname', models.CharField(max_length=255)),
                ('contact_function', models.CharField(max_length=255)),
                ('contact_service', models.CharField(max_length=255)),
                ('contact_mail', models.CharField(max_length=255)),
                ('contact_phone', models.CharField(max_length=255)),
                ('update', models.DateTimeField(auto_now=True)),
                ('creation', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Department')),
                ('interventions', models.ManyToManyField(through='projects.InterventionType', to='projects.Intervention')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Manager')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('insee', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StakeHolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StakeHolderType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('stakeholder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.StakeHolder')),
            ],
        ),
        migrations.CreateModel(
            name='StructurePosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StructurePositionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=255)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('structure_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.StructurePosition')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='missing_skills',
            field=models.ManyToManyField(related_name='missing_skill', to='projects.Skill'),
        ),
        migrations.AddField(
            model_name='project',
            name='mobilized_skills',
            field=models.ManyToManyField(related_name='mobilized_skill', to='projects.Skill'),
        ),
        migrations.AddField(
            model_name='project',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Region'),
        ),
        migrations.AddField(
            model_name='project',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Schedule'),
        ),
        migrations.AddField(
            model_name='project',
            name='stakeholders',
            field=models.ManyToManyField(through='projects.StakeHolderType', to='projects.StakeHolder'),
        ),
        migrations.AddField(
            model_name='project',
            name='structure_positions',
            field=models.ManyToManyField(through='projects.StructurePositionType', to='projects.StructurePosition'),
        ),
        migrations.AddField(
            model_name='interventiontype',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]