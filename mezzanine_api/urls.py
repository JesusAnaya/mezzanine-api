from django.conf.urls import patterns, url, include
from rest_framework import routers
from mezzanine.pages.models import Page
from .views import MezzanineViewSets


class MezzanineAPIRouter(object):
    router = routers.DefaultRouter()

    def __init__(self):
        for root_name, viewset in MezzanineViewSets().iteritems():
            self.router.register(root_name, viewset)

    def get_urls(self):
        return  self.router.urls


urlpatterns = patterns('',
    url(r'^', include(MezzanineAPIRouter().get_urls())),
)
