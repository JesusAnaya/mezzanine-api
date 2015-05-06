from rest_framework.serializers import ModelSerializer


class MutableModelSerializer(ModelSerializer):
    @classmethod
    def create(cls, model):
        class_name = '{}Serializer'.format(model.__name__)
        attrs = {
            'Meta': type('Meta', (), {
                'model': model,
                'exclude': []
            })
        }
        return type(class_name, (MutableModelSerializer,), attrs)
