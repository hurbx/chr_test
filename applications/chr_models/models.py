from django.contrib.postgres.fields import ArrayField
from django.db import models

"""Modelos de la Aplicacion"""


class Company(models.Model):
    """Modelo Empresa BikeSantiago"""
    name = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)

    company = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.name} - {self.country} - {self.latitude} - {self.longitude}'


class Stations(models.Model):
    """Modelo Sucursales BikeSantiago"""
    empty_slots = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    ebikes = models.IntegerField(blank=True, null=True)
    has_ebikes = models.CharField(max_length=30, blank=True, null=True)
    normal_bikes = models.IntegerField(blank=True, null=True)
    last_updated = models.IntegerField(blank=True, null=True)
    payment = ArrayField(models.CharField(max_length=20, blank=True, null=True))

    id_bike = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    time_stamp = models.DateTimeField(blank=True, null=True)

    exist = models.BooleanField(blank=True, null=True)
    post_code = models.CharField(max_length=20, blank=True, null=True)
    renting = models.IntegerField(blank=True, null=True)
    returning = models.IntegerField(blank=True, null=True)
    slots = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    stations = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.slots} - {self.address} - {self.altitude} - {self.ebikes} - {self.has_ebikes} - ' \
               f'{self.normal_bikes} - {self.last_updated} - {self.payment}, {self.id_bike} - {self.name} - ' \
               f'{self.quantity} - {self.latitude} - {self.longitude} - {self.time_stamp} - {self.exist} - ' \
               f'{self.post_code} - {self.renting} - {self.returning} - {self.slots} - {self.uid}'


class TableData(models.Model):
    name = models.URLField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(max_length=20, blank=True, null=True)
    typology = models.CharField(max_length=20, blank=True, null=True)
    titular = models.CharField(max_length=100, blank=True, null=True)
    inversion = models.CharField(max_length=20, blank=True, null=True)
    date = models.CharField(max_length=40, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    map = models.CharField(max_length=30, default='sin informacion', blank=True, null=True)

    table = models.Manager()

    def __str__(self):
        return f'{self.id} - {self.name} - {self.type} - {self.region} - {self.typology} - {self.titular} - {self.inversion} - {self.date} - {self.map}'
