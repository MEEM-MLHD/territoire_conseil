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


class ProjectAdmin(admin.ModelAdmin):
    inlines = (LeaderInline, StakeHolderTypeInline, )
    fieldsets = (
        (None, {'fields': ('name', 'description')}),
        (u"Périmètre du projet", {'fields':
            ('region',
             'department',
             ('epci_name', 'epci_siren'),
             ('town_name', 'town_insee'),
             'geom',
            )
            }),
        (u"Référents", {'fields': ('referents', )}),
        (u"Thèmatiques", {'fields': ('themes', 'themes_others' )}),
        (u"Pilotage de la mission d'appui", {'fields': ('manager', 'manager_other')}),
        (u"Eléments déclencheur", {'fields': ('triggers', 'triggers_others')}),
        (u"Types d'interventions", {'fields': ('interventions', 'interventions_others')}),
        (u"Missions", {'fields': ('structure_challenges', )}),
        (u"Compétences de la structure", {'fields': ('mobilized_skills', 'mobilized_skills_others', 'missing_skills', 'missing_skills_others')}),
        (u"Calendrier", {'fields': ('schedule', )}),
        (u"Conditions de réussite, blocages et solutions", {'fields': ('obstables', )}),
    )


admin.site.register(Region)
admin.site.register(Referent)
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
