from django.test import TestCase
from mock import MagicMock
from mezzanine_rest.viewsets import MutableModelViewSet


class TestViewSets(TestCase):
    def setUp(self):
        pass

    def test_create_a_mutable_viewset(self):
        serializer_class = MagicMock(name='serializer_class')
        model = MagicMock(name='model')
        model.__name__ = 'BlogPost'
        model.objects.all.return_value = []

        viewset_class = MutableModelViewSet.create(model, serializer_class)
        viewset = viewset_class()
        self.assertEqual(viewset.queryset, [])
        self.assertEqual(viewset.serializer_class, serializer_class)
