# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin

from projects.views import add, home, profile


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add/$', add, name='add'),
    url(r'^$', home, name='home'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile/', profile, name='profile'),
]

admin.site.site_header = "Conseil aux territoires"
