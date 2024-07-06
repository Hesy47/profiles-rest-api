from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serializes a name field to testing our APIview"""

    name = serializers.CharField(max_length=10)
