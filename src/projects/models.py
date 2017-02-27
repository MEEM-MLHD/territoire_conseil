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


# class Skill(models.Model):
#     label = models.CharField(max_length=255)

#     class Meta:
#         verbose_name = u"Compétence"

#     def __unicode__(self):
#         return self.label


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
    begin = models.DateField(u"Date de début de projet", blank=True, null=True)
    end = models.DateField(u"Date prévisionnelle de fin de projet", blank=True, null=True)
    image = models.ImageField(upload_to="image", null=True, blank=True)
    url = models.URLField("Pour en savoir plus (lien URL)", blank=True)

    region = models.ForeignKey(Region, verbose_name="Région", blank=True, null=True)
    department = models.ForeignKey(Department, verbose_name="Département", blank=True, null=True)
    epci_name = models.CharField("Nom de l'EPCI", max_length=255, blank=True)
    epci_siren = models.CharField("N° SIREN de l'EPCI", max_length=255, blank=True)
    town_name = models.CharField("Non de la commune", max_length=255, blank=True)
    town_insee = models.CharField("Code INSEE de la commune", max_length=255, blank=True)
    land = models.CharField("Non du Pays/PETR", max_length=255, blank=True)
    geom = models.GeometryField(u"Dessiner le contour du projet", blank=True, null=True)
    shapefile = models.FileField(u"ou importer un ficher shape", upload_to='shapefile/', blank=True, null=True)

    referents = models.ManyToManyField('Referent')

    themes = models.ManyToManyField(Theme, verbose_name=u"Thématiques")
    themes_others = models.CharField(u"Autres thématiques", max_length=255, blank=True)


    triggers = models.ManyToManyField(Trigger, verbose_name=u"Eléments déclencheur")
    triggers_others = models.CharField(u"Autres éléments déclencheurs", max_length=255, blank=True)

    interventions = models.ManyToManyField(Intervention)
    interventions_others = models.CharField(u"Autres interventions", max_length=255, blank=True)

    structure_challenges = models.TextField(u"Missions / enjeux pour votre structure (5 lignes max.)", blank=True)

    # mobilized_skills = models.ManyToManyField(Skill, verbose_name=u"Compétences mobilisées", related_name="mobilized_skill")
    # mobilized_skills_others = models.CharField(u"Autres compétences mobilisées", max_length=255, blank=True)
    # missing_skills = models.ManyToManyField(Skill, verbose_name=u"Compétences manquantes", related_name="missing_skill")
    # missing_skills_others = models.CharField(u"Autres compétences manquantes", max_length=255, blank=True)

    schedule = models.ForeignKey(Schedule, verbose_name="Calendrier d'accompagnement")

    STATE_CHOICES = (
        ('in_progress', 'en cours'),
        ('completed', u'achevé'),
    )

    state = models.CharField(u"Etat du projet", choices=STATE_CHOICES, max_length=12, default='in_progress')
    obstables = models.TextField(u"", blank=True, help_text="10 lignes max.")

    stakeholders = models.ManyToManyField(StakeHolder, through='StakeHolderType')

    comments = models.TextField(u"", blank=True)

    attachment = models.FileField(u"Pièce jointe", upload_to="attachment/", null=True, blank=True)

    update = models.DateTimeField(auto_now=True)
    creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Projet"

    def __unicode__(self):
        return self.name


class Leader(models.Model):
    PROJECT_LEADER_TYPE_CHOICES = (
        ('public', 'Public'),
        ('private', u'Privé'),
    )

    type = models.CharField("Type de porteur de projet", choices=PROJECT_LEADER_TYPE_CHOICES, max_length=255, null=False, blank=False)
    name = models.CharField("Nom du porteur de projet", max_length=255, blank=True)
    project = models.ForeignKey(Project)


class Referent(models.Model):
    firstname = models.CharField(u"Prénom", max_length=255, blank=True)
    lastname = models.CharField(u"Nom", max_length=255)
    function = models.CharField(u"Fonction", max_length=255, blank=True)
    structure = models.ForeignKey(Structure, verbose_name="Structure")
    service = models.CharField(u"Service", max_length=255, blank=True, help_text=u"Eviter les sigles")
    mail = models.CharField(u"Mail", max_length=255)
    phone = models.CharField(u"Téléphone", max_length=255, blank=True)


class StakeHolderType(models.Model):
    stakeholder = models.ForeignKey(StakeHolder, verbose_name="Acteur")
    project = models.ForeignKey(Project)
    detail = models.CharField(max_length=255)
    manager = models.BooleanField("Pilote", default=None)
