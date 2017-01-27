from django.shortcuts import render
from django.forms import formset_factory

from .forms import ProjectForm, ReferentForm, StakeHolderTypeForm


def add(request):
    form = ProjectForm()
    referent_formset = formset_factory(ReferentForm)
    stakeholdertype_formset = formset_factory(StakeHolderTypeForm)
    return render(request, 'add.html', {
        'form': form,
        'referent_formset': referent_formset,
        'stakeholdertype_formset': stakeholdertype_formset
    })

