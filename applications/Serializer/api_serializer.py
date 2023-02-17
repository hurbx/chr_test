

from rest_framework import serializers
from applications.chr_models.models import Stations


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stations
        fields = '__all__'
