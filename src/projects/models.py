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


class Trigger(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        verbose_name = u"Elément déclencheur"

    def __unicode__(self):
        return self.label


class Schedule(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        verbose_name = u"Calendrier"

    def __unicode__(self):
        return self.label


class Theme(models.Model):
    label = models.CharField(max_length=255)

    class Meta:
        verbose_name = u"Thématique"

    def __unicode__(self):
        return self.label


class Structure(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField("Nom du projet", max_length=255)

    description = models.TextField("Description du projet", blank=True, help_text="5 lignes maximum")

    PROJECT_LEADER_TYPE_CHOICES = (
        ('public', 'Public'),
        ('private', u'Privé'),
    )

    project_leader_type = models.CharField("Type de porteur de projet", choices=PROJECT_LEADER_TYPE_CHOICES, max_length=255, null=False, blank=False)
    project_leader_name = models.CharField("Nom du porteur de projet", max_length=255, blank=True)

    region = models.ForeignKey(Region, verbose_name="Région", blank=True, null=True)
    department = models.ForeignKey(Department, verbose_name="Département", blank=True, null=True)
    epci_name = models.CharField("Nom de l'EPCI", max_length=255, blank=True)
    epci_siren = models.CharField("N° SIREN de l'EPCI", max_length=255, blank=True)
    town_name = models.CharField("Non de la commune", max_length=255, blank=True)
    town_insee = models.CharField("Code INSEE de la commune", max_length=255, blank=True)
    geom = models.GeometryField(u"Périmètre SIG", blank=True, null=True)

    referents = models.ManyToManyField('Referent')

    themes = models.ManyToManyField(Theme, verbose_name=u"Thématiques")
    themes_others = models.CharField(u"Autres thématiques", max_length=255, blank=True)

    manager = models.ForeignKey(Manager, verbose_name="Pilote", blank=True, null=True)
    manager_other = models.CharField(u"Autre pilote, préciser", max_length=255, blank=True)

    triggers = models.ManyToManyField(Trigger, verbose_name=u"Eléments déclencheur")
    triggers_others = models.CharField(u"Autres éléments déclencheurs", max_length=255, blank=True)

    interventions = models.ManyToManyField(Intervention)
    interventions_others = models.CharField(max_length=255, blank=True)

    structure_challenges = models.TextField(u"Missions / enjeux pour votre structure (5 lignes max.)", blank=True)

    mobilized_skills = models.ManyToManyField(Skill, verbose_name=u"Compétences mobilisées", related_name="mobilized_skill")
    mobilized_skills_others = models.CharField(u"Autres compétences mobilisées", max_length=255, blank=True)
    missing_skills = models.ManyToManyField(Skill, verbose_name=u"Compétences manquantes", related_name="missing_skill")
    missing_skills_others = models.CharField(u"Autres compétences manquantes", max_length=255, blank=True)

    schedule = models.ForeignKey(Schedule, verbose_name="Calendrier d'accompagnement")
    obstables = models.TextField(u"Blocages rencontrés, comment ont été levés les blocages (10 lignes max.)", blank=True)

    stakeholders = models.ManyToManyField(StakeHolder, through='StakeHolderType')

    update = models.DateTimeField(auto_now=True)
    creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Projet"

    def __unicode__(self):
        return self.name


class Referent(models.Model):
    firstname = models.CharField(u"Prénom", max_length=255, blank=True)
    lastname = models.CharField(u"Nom", max_length=255)
    function = models.CharField(u"Fonction", max_length=255, blank=True)
    structure = models.ForeignKey(Structure, verbose_name="Structure")
    service = models.CharField(u"Service", max_length=255, blank=True)
    mail = models.CharField(u"Mail", max_length=255)
    phone = models.CharField(u"Téléphone", max_length=255, blank=True)


class StakeHolderType(models.Model):
    stakeholder = models.ForeignKey(StakeHolder, verbose_name="Acteur")
    project = models.ForeignKey(Project)
    detail = models.CharField(max_length=255)
