# -*- coding: utf-8 -*-
import django_filters
from django import forms

from .models import Project


class ProjectFilter(django_filters.FilterSet):
    # zonage_insee = django_filters.filters.ModelMultipleChoiceFilter(queryset=ZonageINSEE.objects.all(), widget=forms.CheckboxSelectMultiple, label="Zonage INSEE")
    # type_operations = django_filters.filters.ModelMultipleChoiceFilter(queryset=TypeOperation.objects.all(), widget=forms.CheckboxSelectMultiple, label=u"Type d'opération")
    # label_ecoquartier = django_filters.filters.ModelMultipleChoiceFilter(queryset=LabelEcoQuartier.objects.all(), widget=forms.CheckboxSelectMultiple, label=u"État d'avancement")

    class Meta:
        model = Project
        fields = ['begin', 'end', 'themes', 'triggers', 'interventions', 'state', 'stakeholders',]