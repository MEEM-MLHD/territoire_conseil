# -*- coding: utf-8 -*-
from djgeojson.views import GeoJSONLayerView

from django.conf.urls import url, include
from django.contrib import admin

from projects.views import add, home, profile, detail, update
from projects.models import Project


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add/$', add, name='add'),
    url(r'^update/(?P<pk>\d+)$', update, name='update'),
    url(r'^$', home, name='home'),
    url(r'^project/(?P<pk>\d+)$', detail, name='detail'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile/', profile, name='profile'),
	# url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Project, geometry_field='geom', properties=('name', 'geom',)), name='data'),
]

admin.site.site_header = "Conseil aux territoires"
