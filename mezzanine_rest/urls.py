from rest_framework import routers
from django.db.models.loading import get_model
from mezzanine.conf import settings
from mezzanine_rest.serializers import MutableModelSerializer
from mezzanine_rest.viewsets import MutableModelViewSet
from copy import deepcopy

class DynamicAPIRouter(object):
    router = routers.SimpleRouter()

    def __init__(self):
        for path, viewset in self.autodiscover():
            self.router.register(path, viewset)

    def autodiscover(self):
        results = {}
        for root_name, values in settings.MEZZANINE_REST_SETTINGS.iteritems():
            for app_model in values:
                app_name, model_name = app_model.split('.')
                model = get_model(app_name, model_name)

                serializer_class = MutableModelSerializer.create(model)
                viewset = MutableModelViewSet.create(model, serializer_class)

                print "Model: ", model.__name__, " viewset: ", viewset.queryset

                results.update({
                    '%s/%s' % (root_name.lower(), model_name.lower()): viewset
                })
        return results.iteritems()

    def get_urls(self):
        return self.router.urls


urlpatterns = DynamicAPIRouter().get_urls()
