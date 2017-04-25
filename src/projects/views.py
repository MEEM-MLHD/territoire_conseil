import json
import requests
from djgeojson.serializers import Serializer as GeoJSONSerializer

from django.shortcuts import render, redirect
from django.forms import formset_factory, inlineformset_factory, modelformset_factory
from django.views.decorators.cache import never_cache
from django.contrib.gis.geos import GEOSGeometry, GeometryCollection

from .filters import ProjectFilter
from .forms import ProjectForm, ReferentForm, StakeHolderTypeForm, LeaderForm
from .models import Project, Referent, StakeHolderType, Leader, Department, Region


def home(request):
    queryset = Project.objects.all().order_by('-update')
    f = ProjectFilter(request.GET, queryset=queryset)
    geojson = GeoJSONSerializer().serialize(f.qs,
          geometry_field='geom',
          properties=('name', 'detail_url', 'feature_image', ))

    return render(request, 'home.html', {'filter': f, 'geojson': geojson})


def profile(request):
    user = request.user
    # projects_owner = Project.objects.filter(owner=request.user)
    # projects_editor = Project.objects.filter(editors=request.user)
    return render(request, 'profile.html', {
        'user': user,
        # 'projects_owner': projects_owner,
        # 'projects_editor': projects_editor
    })


def detail(request, pk):
    project = Project.objects.get(id=pk)
    geojson = GeoJSONSerializer().serialize([project, ],
          geometry_field='geom',
          properties=('name', 'detail_url', 'feature_image', ))

    return render(request, 'detail.html', {
        'project': project,
        'geojson': geojson,
    })


@never_cache
def add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            if project.town_insee:
                # town_insee
                r = requests.get('https://geo.api.gouv.fr/communes?code=%s&fields=contour,departement,region' % (project.town_insee))
                data = r.json()[0]
                coord = data['contour']
                mpoly = GEOSGeometry(json.dumps(coord))
                project.geom = GeometryCollection(mpoly)

                department_name = data['departement']['nom']
                department_insee = data['departement']['code']
                departement, created = Department.objects.get_or_create(name=department_name, insee=department_insee)
                project.department = departement

                region_name = data['region']['nom']
                region_insee = data['region']['code']
                region, created = Region.objects.get_or_create(name=region_name, insee=region_insee)
                project.region = region
            elif project.department:
                project.geom = project.department.geom
            elif project.region:
                project.geom = project.region.geom


            project.save()


            ReferentFormSet = inlineformset_factory(Project, Referent, form=ReferentForm, extra=0, can_delete=True)
            referent_formset = ReferentFormSet(request.POST, request.FILES, instance=project)

            StakeHolderTypeFormset = inlineformset_factory(Project, StakeHolderType, form=StakeHolderTypeForm, extra=0, can_delete=True)
            stakeholdertype_formset = StakeHolderTypeFormset(request.POST, request.FILES, instance=project)

            LeaderFormset = inlineformset_factory(Project, Leader, form=LeaderForm, extra=0, can_delete=True)
            leader_formset = LeaderFormset(request.POST, request.FILES, instance=project)

            if referent_formset.is_valid():
                referent_formset.save()
            if stakeholdertype_formset.is_valid():
                stakeholdertype_formset.save()
            if leader_formset.is_valid():
                leader_formset.save()

            return redirect('detail', pk=project.id)


    form = ProjectForm()
    referent_formset = inlineformset_factory(Project, Referent, form=ReferentForm, extra=0, can_delete=True)
    stakeholdertype_formset = inlineformset_factory(Project, StakeHolderType, form=StakeHolderTypeForm, extra=0, can_delete=True)
    leader_formset = inlineformset_factory(Project, Leader, form=LeaderForm, extra=0, can_delete=True)

    return render(request, 'add.html', {
        'form': form,
        'referent_formset': referent_formset,
        'stakeholdertype_formset': stakeholdertype_formset,
        'leader_formset': leader_formset,
    })


@never_cache
def update(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            if project.town_insee:
                # town_insee
                r = requests.get('https://geo.api.gouv.fr/communes?code=%s&fields=contour,departement,region' % (project.town_insee))
                data = r.json()[0]
                coord = data['contour']
                mpoly = GEOSGeometry(json.dumps(coord))
                project.geom = GeometryCollection(mpoly)

                department_name = data['departement']['nom']
                department_insee = data['departement']['code']
                departement, created = Department.objects.get_or_create(name=department_name, insee=department_insee)
                project.department = departement

                region_name = data['region']['nom']
                region_insee = data['region']['code']
                region, created = Region.objects.get_or_create(name=region_name, insee=region_insee)
                project.region = region

            project.save()

            ReferentFormSet = inlineformset_factory(Project, Referent, form=ReferentForm, extra=0, can_delete=True)
            referent_formset = ReferentFormSet(request.POST, request.FILES, instance=project)

            StakeHolderTypeFormset = inlineformset_factory(Project, StakeHolderType, form=StakeHolderTypeForm, extra=0, can_delete=True)
            stakeholdertype_formset = StakeHolderTypeFormset(request.POST, request.FILES, instance=project)

            LeaderFormset = inlineformset_factory(Project, Leader, form=LeaderForm, extra=0, can_delete=True)
            leader_formset = LeaderFormset(request.POST, request.FILES, instance=project)

            if referent_formset.is_valid():
                referent_formset.save()
            if stakeholdertype_formset.is_valid():
                stakeholdertype_formset.save()
            if leader_formset.is_valid():
                leader_formset.save()

            return redirect('detail', pk=project.id)

    form = ProjectForm(instance=project)

    referent_formset = inlineformset_factory(Project, Referent, form=ReferentForm, extra=0, can_delete=True)
    referent_formset = referent_formset(instance=project)
    stakeholdertype_formset = inlineformset_factory(Project, StakeHolderType, form=StakeHolderTypeForm, extra=0, can_delete=True)
    stakeholdertype_formset = stakeholdertype_formset(instance=project)
    leader_formset = inlineformset_factory(Project, Leader, form=LeaderForm, extra=0, can_delete=True)
    leader_formset = leader_formset(instance=project)

    return render(request, 'update.html', {
        'project': project,
        'form': form,
        'referent_formset': referent_formset,
        'stakeholdertype_formset': stakeholdertype_formset,
        'leader_formset': leader_formset,
    })
