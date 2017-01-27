from django import forms
from leaflet.forms.widgets import LeafletWidget

from .models import Project, Referent, StakeHolderType


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        exclude = ('referents', )
        widgets = {'geom': LeafletWidget(),
        		   'interventions': forms.CheckboxSelectMultiple,
        		   'themes': forms.CheckboxSelectMultiple,
        		   'triggers': forms.CheckboxSelectMultiple,
        		   'mobilized_skills': forms.CheckboxSelectMultiple,
        		   'missing_skills': forms.CheckboxSelectMultiple,
        			}


class ReferentForm(forms.ModelForm):

	class Meta:
		model = Referent
		fields = '__all__'


class StakeHolderTypeForm(forms.ModelForm):

	class Meta:
		model = StakeHolderType
		exclude = ('project', )