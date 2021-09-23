from django.core import serializers


def json_stringify(data=None):
    if data:
        return serializers.serialize('json', data)