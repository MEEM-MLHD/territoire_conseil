# -*- coding: utf-8 -*-
from django import forms
from leaflet.forms.widgets import LeafletWidget
from djangoformsetjs.utils import formset_media_js

from .models import Project, Referent, StakeHolderType, Leader


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        exclude = ('referents', 'stakeholders')
        widgets = {'geom': LeafletWidget(),
               'interventions': forms.CheckboxSelectMultiple,
               'themes': forms.CheckboxSelectMultiple,
               'triggers': forms.CheckboxSelectMultiple,
               'description': forms.Textarea({'rows': 5}),
               'structure_challenges': forms.Textarea({'rows': 5})
                }


class ReferentForm(forms.ModelForm):

    class Meta:
        model = Referent
        fields = '__all__'


class StakeHolderTypeForm(forms.ModelForm):

    class Meta:
        model = StakeHolderType
        exclude = ('project', )


class LeaderForm(forms.ModelForm):

    PROJECT_LEADER_TYPE_CHOICES = (
        ('public', 'Public'),
        ('private', u'Privé'),
    )

    type = forms.CharField(label="", max_length=99, required=True, widget=forms.RadioSelect(choices=PROJECT_LEADER_TYPE_CHOICES))

    class Meta:
        model = Leader
        exclude = ('project', )