# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import *


class InterventionTypeInline(admin.TabularInline):
    model = InterventionType
    extra = 1
    verbose_name = "Type d'intervention"
    verbose_name_plural = "Types d'intervention"


class StakeHolderTypeInline(admin.TabularInline):
    model = StakeHolderType
    extra = 1
    verbose_name = "Acteur de l'ingénierie mobilisé"
    verbose_name_plural = "Acteurs de l'ingénierie mobilisés"


class StructurePositionTypeInline(admin.TabularInline):
    model = StructurePositionType
    extra = 1
    verbose_name = "Positionnement de votre structure par rapport au porteur de projet"
    verbose_name_plural = "Positionnements de votre structure par rapport au porteur de projet"


class ProjectAdmin(admin.ModelAdmin):
    inlines = (StakeHolderTypeInline, InterventionTypeInline, StructurePositionTypeInline)
    fieldsets = (
        (None, {'fields': ('name', 'description')}),
        (u"Périmètre", {'fields':
            ('region',
             'department',
             ('epci_name', 'epci_siren'),
             ('town_name', 'town_insee'),
             'other_perimeter',
             'geom',
            )
            }),
        (u"Référent DDT", {'fields': ('ddt_reference_name', 'ddt_reference_service')}),
        (u"Thèmatiques", {'fields': ('themes', )}),
        (u"Pilotage", {'fields': ('manager', 'manager_other', 'manager_detail')}),
        (u"Missions", {'fields': ('structure_challenges', )}),
        (u"Compétences", {'fields': ('mobilized_skills', 'missing_skills')}),
        (u"Calendrier", {'fields': ('schedule', )}),
        (u"Obstacles", {'fields': ('obstables', )}),
        (u"Contact", {'fields': (('contact_firstname', 'contact_lastname'), ('contact_service', 'contact_function'), ('contact_mail', 'contact_phone'))}),
    )


admin.site.register(Region)
admin.site.register(Department)
admin.site.register(Intervention)
admin.site.register(StakeHolder)
admin.site.register(StructurePosition)
admin.site.register(Manager)
admin.site.register(Skill)
admin.site.register(Schedule)
admin.site.register(Project, ProjectAdmin)