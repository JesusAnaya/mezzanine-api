from rest_framework.viewsets import ModelViewSet


class MutableModelViewSet(object):
    @classmethod
    def create(cls, model, serializer_class):
        class_name = '{}ViewSet'.format(model.__name__)
        attrs = {
            'queryset': model.objects.all(),
            'serializer_class': serializer_class
        }
        return type(class_name, (ModelViewSet,), attrs)
