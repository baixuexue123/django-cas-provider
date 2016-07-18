# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from views import login, validate, logout

urlpatterns = patterns('',
    url(r'^login/', login),
    url(r'^validate/', validate),
    url(r'^logout/', logout),
)
