from rest_framework import serializers
from applications.chr_models.models import TableData


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableData
        fields = '__all__'
