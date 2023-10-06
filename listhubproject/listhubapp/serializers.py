# appname/serializers.py
from rest_framework import serializers
from .models import ListHubProperty


class ListHubPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ListHubProperty
        fields = '__all__'
