# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models
from django.core.urlresolvers import reverse


class Region(models.Model):
    name = models.CharField(max_length=255)
    insee = models.CharField(max_length=255)
    geom = models.GeometryField(blank=True, null=True)

    class Meta:
        verbose_name = u"Région"
        ordering = ['name', ]

    def __unicode__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)
    insee = models.CharField(max_length=255)
    geom = models.GeometryField(blank=True, null=True)
    region = models.ForeignKey(Region, blank=True, null=True)

    class Meta:
        verbose_name = u"Département"
        ordering = ['name', ]

    def __unicode__(self):
        return self.name


class Intervention(models.Model):
    label = models.CharField(max_length=255)
    order = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Intervention"
        ordering = ['order', ]

    def __unicode__(self):
        return self.label


class StakeHolder(models.Model):
    label = models.CharField(max_length=255)
    order = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Acteur"
        ordering = ['order', ]

    def __unicode__(self):
        return self.label


class Manager(models.Model):
    label = models.CharField(max_length=255)
    order = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = u"Pilote"
        ordering = ['order', ]

    def __unicode__(self):
        return self.label


class Trigger(models.Model):
    label = models.CharField(max_length=255)
    order = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = u"Elément déclencheur"
        ordering = ['order', ]

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
    order = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = u"Thématique"
        ordering = ['order', ]

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
    url = models.URLField("Pour en savoir plus", blank=True, help_text="Lien URL")

    region = models.ForeignKey(Region, verbose_name="Région", blank=True, null=True)
    department = models.ForeignKey(Department, verbose_name="Département", blank=True, null=True)
    epci_name = models.CharField("Nom de l'EPCI", max_length=255, blank=True)
    epci_siren = models.CharField("N° SIREN de l'EPCI", max_length=255, blank=True)
    town_name = models.CharField("Non de la commune", max_length=255, blank=True)
    town_insee = models.CharField("Code INSEE de la commune", max_length=255, blank=True)
    land = models.CharField("Non du Pays/PETR", max_length=255, blank=True)
    geom = models.GeometryField(u"Dessiner le contour du projet", blank=True, null=True)
    shapefile = models.FileField(u"ou importer un ficher shape", upload_to='shapefile/', blank=True, null=True)

    themes = models.ManyToManyField(Theme, verbose_name=u"Thématiques", blank=True)
    themes_others = models.CharField(u"Autres thématiques", max_length=255, blank=True)

    funding_european = models.CharField(u"Financement européen", max_length=255, blank=True, help_text=u"Préciser le type de financement européen s'il y a lieu")
    funding_national = models.CharField(u"Financement national", max_length=255, blank=True, help_text=u"Préciser le type de financement national s'il y a lieu")
    funding_regional = models.CharField(u"Financement régional", max_length=255, blank=True, help_text=u"Préciser le type de financement régional s'il y a lieu")
    funding_departmental = models.CharField(u"Financement départemental", max_length=255, blank=True, help_text=u"Préciser le type de financement départemental s'il y a lieu")
    funding_other = models.CharField(u"Autre financement", max_length=255, blank=True, help_text=u"Préciser de quel autre type de financement le projet a bénéficier")

    triggers = models.ManyToManyField(Trigger, verbose_name=u"Eléments déclencheur", blank=True)
    triggers_others = models.CharField(u"Autres éléments déclencheurs", max_length=255, blank=True)

    interventions = models.ManyToManyField(Intervention, blank=True)
    interventions_others = models.CharField(u"Autres interventions", max_length=255, blank=True)

    structure_challenges = models.TextField(u"Missions / enjeux pour votre structure", blank=True, help_text="5 lignes maximum")

    schedule = models.ForeignKey(Schedule, verbose_name="Calendrier d'accompagnement")

    STATE_CHOICES = (
        ('in_progress', 'en cours'),
        ('completed', u'achevé'),
    )

    state = models.CharField(u"Etat du projet", choices=STATE_CHOICES, max_length=12, default='in_progress')
    obstables = models.TextField(u"", blank=True, help_text="10 lignes max.")

    stakeholders = models.ManyToManyField(StakeHolder, verbose_name=u"Acteurs de l'ingénierie mobilisés", through='StakeHolderType', blank=True)

    comments = models.TextField(u"", blank=True)

    attachment = models.FileField(u"Pièce jointe", upload_to="attachment/", null=True, blank=True)

    update = models.DateTimeField(auto_now=True)
    creation = models.DateTimeField(auto_now_add=True)

    @property
    def detail_url(self):
        return reverse('detail', kwargs={'pk':self.id})

    @property
    def feature_image(self):
        if self.image:
            return self.image.url
        return None

    @property
    def geographic_zone(self):
        if self.town_name:
            return u"Ville : %s " % self.town_name
        elif self.department:
            return u"Département : %s" % self.department.name
        elif self.region:
            return u"Région : %s" % self.region.name
        else:
            return 'autre'


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
    project = models.ForeignKey(Project, null=True)


class StakeHolderType(models.Model):
    stakeholder = models.ForeignKey(StakeHolder, verbose_name="Acteur")
    project = models.ForeignKey(Project)
    detail = models.CharField(max_length=255)
    manager = models.BooleanField("Pilote", default=None)
