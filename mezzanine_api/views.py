from django.db.models.loading import get_model
from mezzanine.conf import settings
from mezzanine.core.models import Ownable
from rest_framework import viewsets, serializers
from .serializers import DisplayableSerializer

class MezzanineViewSets(dict):
    def __init__(self, *args, **kwargs):
        super(MezzanineViewSets, self).__init__(*args, **kwargs)

        for root_name, values in settings.MEZZANINE_API_SETTINGS.iteritems():
            for app_model in values:
                app_name, model_name = app_model.split('.')
                model = get_model(app_name, model_name)

                custom_serializer = type('%sSerializer' % model_name,
                    (serializers.HyperlinkedModelSerializer,),
                    {
                        'Meta': type('Meta', (), {
                            'model': model,
                            'exclude': ('site', 'user'),
                        }),
                    }
                )

                viewset = type('%sViewset' % model_name,
                    (viewsets.ModelViewSet,),
                    {
                        'queryset': model.objects.all(),
                        'serializer_class': custom_serializer
                    }
                )

                self.update({
                    '%s/%s' % (root_name, model_name.lower()): viewset
                })

 