from rest_framework import serializers
from mezzanine.blog.models import BlogPost


class DisplayableSerializer(serializers.HyperlinkedModelSerializer):
    site = serializers.RelatedField(source='site', required=False)
