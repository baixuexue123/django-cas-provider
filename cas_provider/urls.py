from django.conf.urls import *

from views import *

urlpatterns = patterns('',
    url(r'^login/', login),
    url(r'^validate/', validate),
    url(r'^logout/', logout),
)
