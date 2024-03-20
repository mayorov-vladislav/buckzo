from rest_framework import serializers
from .models import *


class AboutHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['title', 'description']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['description', 'photo', 'name', 'is_visible', 'order']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'post', 'photo', 'is_visible', 'order']


class MainAboutInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainAboutInfo
        fields = ['photo', 'is_visible', 'order']


