# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)
    insee = models.CharField(max_length=255)

    class Meta:
        verbose_name = u"Région"

    def __unicode__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)
    insee = models.CharField(max_length=255)

    class Meta:
        verbose_name = u"Département"

    def __unicode__(self):
        return self.name


class Intervention(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Intervention"

    def __unicode__(self):
        return self.label


class StakeHolder(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Acteur"

    def __unicode__(self):
        return self.label


class StructurePosition(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Positionnement"

    def __unicode__(self):
        return self.label


class Manager(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        verbose_name = u"Pilote"

    def __unicode__(self):
        return self.label


class Skill(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        verbose_name = u"Compétence"

    def __unicode__(self):
        return self.label


class Schedule(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        verbose_name = u"Calendrier"

    def __unicode__(self):
        return self.label


class Project(models.Model):
    name = models.CharField("Nom", max_length=255)
    region = models.ForeignKey(Region, verbose_name="Région", blank=True, null=True)
    department = models.ForeignKey(Department, verbose_name="Département", blank=True, null=True)
    epci_name = models.CharField("Nom de l'EPCI", max_length=255, blank=True)
    epci_siren = models.CharField("N° SIREN de l'EPCI", max_length=255, blank=True)
    town_name = models.CharField("Non de la commune", max_length=255, blank=True)
    town_insee = models.CharField("Code INSEE de la commune", max_length=255, blank=True)
    other_perimeter = models.CharField(u"Autre périmètre (à préciser)", max_length=255, blank=True)
    geom = models.GeometryField(u"Périmètre SIG", blank=True, null=True)

    description = models.TextField("Description du projet en 5 lignes max.", blank=True)
    ddt_reference_name = models.CharField(u"Nom", max_length=255, blank=True)
    ddt_reference_service = models.CharField(u"Service", max_length=255, blank=True)
    interventions = models.ManyToManyField(Intervention, through='InterventionType')
    interventions_others = models.CharField(max_length=255, blank=True)
    themes = models.TextField(u"Thématiques / portes d'entrée dominantes (production de logement, transition énergétique, accessibilité, revitalisation de centre-bourg, etc.)", blank=True)

    manager = models.ForeignKey(Manager, verbose_name="Pilote", blank=True, null=True)
    manager_other = models.CharField(u"Autre pilote, préciser", max_length=255, blank=True)
    manager_detail = models.TextField(u"Précision sur le pilotage", blank=True)

    stakeholders = models.ManyToManyField(StakeHolder, through='StakeHolderType')
    structure_positions = models.ManyToManyField(StructurePosition, through='StructurePositionType')
    structure_challenges = models.TextField(u"Missions / enjeux pour votre structure (5 lignes max.)", blank=True)
    mobilized_skills = models.ManyToManyField(Skill, verbose_name=u"Compétences mobilisées", related_name="mobilized_skill")
    missing_skills = models.ManyToManyField(Skill, verbose_name=u"Compétences manquantes", related_name="missing_skill")

    schedule = models.ForeignKey(Schedule, verbose_name="Calendrier d'accompagnement")

    obstables = models.TextField(u"Blocages rencontrés, comment ont été levés les blocages (10 lignes max.)", blank=True)

    contact_firstname = models.CharField(u"Prénom", max_length=255, blank=True)
    contact_lastname = models.CharField(u"Nom", max_length=255, blank=True)
    contact_function = models.CharField(u"Fonction", max_length=255, blank=True)
    contact_service = models.CharField(u"Service", max_length=255, blank=True)
    contact_mail = models.CharField(u"Mail", max_length=255, blank=True)
    contact_phone = models.CharField(u"Téléphone", max_length=255, blank=True)

    update = models.DateTimeField(auto_now=True)
    creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Projet"

    def __unicode__(self):
        return self.name


class InterventionType(models.Model):
    intervention = models.ForeignKey(Intervention, verbose_name="Intervention")
    project = models.ForeignKey(Project)
    detail = models.CharField(max_length=255)


class StakeHolderType(models.Model):
    stakeholder = models.ForeignKey(StakeHolder, verbose_name="Acteur")
    project = models.ForeignKey(Project)
    detail = models.CharField(max_length=255)


class StructurePositionType(models.Model):
    structure_position = models.ForeignKey(StructurePosition, verbose_name="Positionnement")
    project = models.ForeignKey(Project)
    detail = models.CharField(max_length=255)
