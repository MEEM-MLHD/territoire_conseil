from django.shortcuts import render
from django.forms import formset_factory

from .forms import ProjectForm, ReferentForm, StakeHolderTypeForm, LeaderForm


def add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()

    form = ProjectForm(request.POST)
    referent_formset = formset_factory(ReferentForm)
    stakeholdertype_formset = formset_factory(StakeHolderTypeForm)
    leader_formset = formset_factory(LeaderForm)

    return render(request, 'add.html', {
        'form': form,
        'referent_formset': referent_formset,
        'stakeholdertype_formset': stakeholdertype_formset,
        'leader_formset': leader_formset,
    })

