# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import login, validate, logout

urlpatterns = [
    url(r'^login/', login),
    url(r'^validate/', validate),
    url(r'^logout/', logout),
]
