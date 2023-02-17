from rest_framework.views import APIView
from applications.Serializer.api_serializer import ApiSerializer
from rest_framework import generics

from applications.chr_models.models import Stations

"""Vista que activa la funcion get_api_data y la guarda en la base de datos"""


class DataBaseInfo(generics.ListCreateAPIView):

    serializer_class = ApiSerializer

    def get_queryset(self):
        queryset = Stations.stations.all()


        return queryset










