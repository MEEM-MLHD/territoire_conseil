# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import *


class StakeHolderTypeInline(admin.TabularInline):
    model = StakeHolderType
    extra = 1
    verbose_name = "Acteur de l'ingénierie mobilisé"
    verbose_name_plural = "Acteurs de l'ingénierie mobilisés"


class LeaderInline(admin.TabularInline):
    model = Leader
    extra = 1
    verbose_name = "Porteur de projet"
    verbose_name_plural = "Porteurs de projet"


class ReferentInline(admin.TabularInline):
    model = Referent
    extra = 1
    verbose_name = "Personne en charge du dossier"
    verbose_name_plural = "Personnes en charge du dossier"


class ProjectAdmin(admin.ModelAdmin):
    inlines = (LeaderInline, ReferentInline, StakeHolderTypeInline, )
    fieldsets = (
        (None, {'fields': ('name', 'description', 'image', 'begin', 'end', 'url')}),
        (u"Périmètre du projet", {'fields':
            ('region',
             'department',
             'land',
             ('epci_name', 'epci_siren'),
             ('town_name', 'town_insee'),
             'geom',
             'shapefile',
            )
            }),
        (u"Thèmatiques", {'fields': ('themes', 'themes_others' )}),
        (u"Eléments déclencheur", {'fields': ('triggers', 'triggers_others')}),
        (u"Types d'interventions", {'fields': ('interventions', 'interventions_others')}),
        (u"Missions", {'fields': ('structure_challenges', )}),
        (u"Calendrier", {'fields': ('schedule', 'state')}),
        (u"Conditions de réussite, blocages et solutions", {'fields': ('obstables', )}),
        (u'Commentaire, autre', {'fields': ('comments', 'attachment')})
    )


admin.site.register(Region)
#admin.site.register(Referent)
admin.site.register(Department)
admin.site.register(Intervention)
admin.site.register(StakeHolder)
admin.site.register(Manager)
#admin.site.register(Skill)
admin.site.register(Theme)
admin.site.register(Trigger)
admin.site.register(Schedule)
admin.site.register(Structure)
admin.site.register(Project, ProjectAdmin)
