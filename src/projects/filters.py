# -*- coding: utf-8 -*-
import django_filters
from django import forms

from .models import Project, Theme, Intervention, StakeHolder, Trigger


class ProjectFilter(django_filters.FilterSet):
    STATE_CHOICES = (
        ('in_progress', 'en cours'),
        ('completed', u'achevé'),
    )

    themes = django_filters.ModelMultipleChoiceFilter(name='themes', queryset=Theme.objects.all(), label= u"Thématiques", help_text='')
    interventions = django_filters.ModelMultipleChoiceFilter(name='interventions', queryset=Intervention.objects.all(), label=u"Interventions", help_text='')
    stakeholders = django_filters.ModelMultipleChoiceFilter(name='stakeholders', queryset=StakeHolder.objects.all(), label=u"Acteurs de l'ingénierie mobilisés", help_text='')
    triggers = django_filters.ModelMultipleChoiceFilter(name='triggers', queryset=Trigger.objects.all(), label=u"Eléments déclencheur", help_text='')
    begin = django_filters.NumberFilter(name='begin', lookup_expr='year__gte', label=u"Année de début de projet", help_text='')
    end = django_filters.NumberFilter(name='end', lookup_expr='year__lte', label=u"Année de fin de projet", help_text='')
    state = django_filters.ChoiceFilter(choices=STATE_CHOICES, label=u"Etat du projet", help_text='')

    class Meta:
        model = Project
        fields = []
