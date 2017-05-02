# -*- coding: utf-8 -*-
import django_filters

from django import forms
from django.core.validators import EMPTY_VALUES

from .models import Project, Theme, Intervention, StakeHolder, Trigger


class EmptyStringFilter(django_filters.BooleanFilter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        value = not value  # well, this is ugly
        exclude = self.exclude ^ (value is False)
        method = qs.exclude if exclude else qs.filter

        return method(**{self.name: ""})


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
    funding_european__isempty = EmptyStringFilter(name='funding_european', label=u"Financement Européen", help_text='')
    funding_national__isempty = EmptyStringFilter(name='funding_national', label=u"Financement National", help_text='')
    funding_regional__isempty = EmptyStringFilter(name='funding_regional', label=u"Financement Régional", help_text='')
    funding_departmental__isempty = EmptyStringFilter(name='funding_departmental', label=u"Financement Départemental", help_text='')

    class Meta:
        model = Project
        fields = []
