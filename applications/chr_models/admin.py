from django.contrib import admin
from .models import Company, Stations, TableData


# Register your models here.
class TableDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'region', 'typology', 'titular', 'inversion', 'date')
    search_fields = ('name', 'type', 'region', 'typology', 'titular', 'inversion', 'date')
    list_filter = ('name',)


admin.site.register(TableData, TableDataAdmin)


class StationsAdmin(admin.ModelAdmin):
    list_display = ('empty_slots', 'address', 'payment', 'last_updated', 'post_code', 'time_stamp', 'company')
    search_fields = ('address', 'payment', 'last_updated', 'post_code', 'time_stamp', 'company')
    list_filter = ('payment',)


admin.site.register(Stations, StationsAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'latitude', 'longitude')
    search_fields = ('name', 'country', 'latitude', 'longitude')
    list_filter = ('name',)


admin.site.register(Company, CompanyAdmin)
