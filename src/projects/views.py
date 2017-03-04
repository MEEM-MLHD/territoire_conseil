from django.shortcuts import render
from django.forms import formset_factory, inlineformset_factory, modelformset_factory
from django.views.decorators.cache import never_cache

from .filters import ProjectFilter
from .forms import ProjectForm, ReferentForm, StakeHolderTypeForm, LeaderForm
from .models import Project, Referent, StakeHolderType, Leader


def home(request):
    queryset = Project.objects.all()
    f = ProjectFilter(request.GET, queryset=queryset)
    return render(request, 'home.html', {'filter': f})


def profile(request):
    user = request.user
    # projects_owner = Project.objects.filter(owner=request.user)
    # projects_editor = Project.objects.filter(editors=request.user)
    return render(request, 'profile.html', {
        'user': user,
        # 'projects_owner': projects_owner,
        # 'projects_editor': projects_editor
    })


@never_cache
def add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()

            ReferentFormSet = inlineformset_factory(Project, Referent, form=ReferentForm, extra=0)
            referent_formset = ReferentFormSet(request.POST, request.FILES, instance=project)

            StakeHolderTypeFormset = inlineformset_factory(Project, StakeHolderType, form=StakeHolderTypeForm, extra=0)
            stakeholdertype_formset = StakeHolderTypeFormset(request.POST, request.FILES, instance=project)

            LeaderFormset = inlineformset_factory(Project, Leader, form=LeaderForm, extra=0)
            leader_formset = LeaderFormset(request.POST, request.FILES, instance=project)

            if referent_formset.is_valid():
                referent_formset.save()
            if stakeholdertype_formset.is_valid():
                stakeholdertype_formset.save()
            if leader_formset.is_valid():
                leader_formset.save()


    form = ProjectForm()
    referent_formset = inlineformset_factory(Project, Referent, form=ReferentForm, extra=0)
    stakeholdertype_formset = inlineformset_factory(Project, StakeHolderType, form=StakeHolderTypeForm, extra=0)
    leader_formset = inlineformset_factory(Project, Leader, form=LeaderForm, extra=0)

    return render(request, 'add.html', {
        'form': form,
        'referent_formset': referent_formset,
        'stakeholdertype_formset': stakeholdertype_formset,
        'leader_formset': leader_formset,
    })

