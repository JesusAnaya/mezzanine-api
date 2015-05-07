from rest_framework.serializers import ModelSerializer


class MutableModelSerializer(object):
    @classmethod
    def create(cls, model):
        class_name = '{0}Serializer'.format(model.__name__)
        attrs = {
            'Meta': type('Meta', (), {
                'model': model,
                'exclude': []
            })
        }
        return type(class_name, (ModelSerializer,), attrs)
