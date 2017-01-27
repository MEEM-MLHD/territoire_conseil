# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin

from projects.views import add


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add/$', add, name='add'),
]

admin.site.site_header = "Conseil aux territoires"
